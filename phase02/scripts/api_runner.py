#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
api_runner.py — GitCode API 测试 runner（确定性）

调用 GitCode REST API（v8/v5），执行断言判定。
凭据：GITCODE_ACCESS_TOKEN（OAuth2 Bearer）或 ~/.gitcode-token。

用法:
    import api_runner as ar
    cfg = ar.ApiConfig(owner="ComputingActionTest", repo="gitcode_api")
    result = ar.run_api_case(cfg, case_id="API-PULLS-01-001",
                             endpoint="/api/v8/repos/{owner}/{repo}/pulls",
                             method="GET", params={"state":"open"},
                             assertions=[...])
"""
import os
import sys
import json
import time
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))


class ApiError(RuntimeError):
    pass


class ApiConfig:
    """API 执行器配置。默认对齐 fixture 仓库（ComputingActionTest/gitcode_api）。"""

    def __init__(self, owner=None, repo=None, api_base=None, token=None):
        self.owner = owner or os.environ.get("GITCODE_OWNER", "ComputingActionTest")
        self.repo = repo or os.environ.get("GITCODE_REPO", "gitcode_api")
        self.api_base = (api_base or os.environ.get("GITCODE_API_BASE_URL",
                                                    "https://gitcode.com")).rstrip("/")
        self.token = token or self._load_token()

    @staticmethod
    def _load_token():
        path = os.path.expanduser(os.environ.get("GITCODE_TOKEN_FILE", "~/.gitcode-token"))
        if os.path.exists(path):
            return open(path, encoding="utf-8").read().strip()
        env = os.environ.get("GITCODE_ACCESS_TOKEN", "")
        if env:
            return env
        raise FileNotFoundError("未找到 GitCode token：既无 ~/.gitcode-token 也无 GITCODE_ACCESS_TOKEN")


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] [API] {msg}", flush=True)


def _resolve_endpoint(endpoint, cfg):
    """替换 endpoint 中的 {owner}/{repo} 占位符。"""
    return endpoint.replace("{owner}", cfg.owner).replace("{repo}", cfg.repo)


def api_call(cfg, endpoint, method="GET", params=None, auth="token"):
    """
    执行一次 API 调用。
    返回 (status_code: int, response_body: dict|str, headers: dict, latency_ms: int)。
    """
    url = cfg.api_base + _resolve_endpoint(endpoint, cfg)
    data = None
    if method in ("POST", "PUT", "PATCH") and params:
        data = json.dumps(params).encode("utf-8")
    elif method == "GET" and params:
        qs = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
        url += ("&" if "?" in url else "?") + qs

    headers = {}
    if auth == "token" and cfg.token:
        headers["Authorization"] = f"Bearer {cfg.token}"
    if data:
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            headers_out = dict(resp.headers)
            try:
                body_parsed = json.loads(body)
            except json.JSONDecodeError:
                body_parsed = body
            return resp.status, body_parsed, headers_out, int((time.time() - t0) * 1000)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        try:
            body_parsed = json.loads(body)
        except Exception:
            body_parsed = body
        return e.code, body_parsed, dict(e.headers), int((time.time() - t0) * 1000)
    except Exception as e:
        raise ApiError(f"{type(e).__name__}: {e}")


def run_api_case(cfg, case_id, endpoint, method="GET", params=None, auth="token",
                 assertions=None):
    """
    执行单条 API 测试用例。
    返回 ApiResult dict（结构同 RunResult，供 assertion_engine.evaluate 消费）。
    """
    t0 = time.time()
    log(f"=== API {case_id} → {method} {endpoint} ===")
    try:
        status_code, body, headers, latency_ms = api_call(cfg, endpoint, method, params, auth)
        log(f"  ← HTTP {status_code} ({latency_ms}ms)")
        body_str = json.dumps(body, ensure_ascii=False) if isinstance(body, (dict, list)) else str(body)
        return {
            "case_id": case_id,
            "status": "COMPLETED",
            "api_status_code": status_code,
            "api_response_body": body,
            "api_response_body_str": body_str,
            "api_response_headers": headers,
            "api_latency_ms": latency_ms,
            "duration_seconds": round(time.time() - t0),
            "logs": body_str,
            "logs_available": True,
        }
    except ApiError as e:
        log(f"  → ENV_ERROR: {e}")
        return {
            "case_id": case_id,
            "status": "ENV_ERROR",
            "reason": str(e),
            "duration_seconds": round(time.time() - t0),
            "logs": "",
            "logs_available": False,
        }


if __name__ == "__main__":
    # 自检：验证可 import 与 token 装载，不触网
    print("api_runner self-check: imports OK")
    try:
        cfg = ApiConfig()
        print(f"  config: {cfg.owner}/{cfg.repo} api={cfg.api_base}")
    except Exception as e:
        print(f"  config load: {type(e).__name__}: {e}")
