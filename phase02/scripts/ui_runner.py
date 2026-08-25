#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui_runner.py — GitCode UI 自动化测试 runner（基于 Playwright）

用法:
    python ui_runner.py <case-yaml> [output-log]

环境变量:
    GITCODE_OWNER       — 目标仓库 owner（默认 weixin_55883847）
    GITCODE_REPO        — 目标仓库名
    GITCODE_UI_BASE_URL — UI 基地址（默认 https://gitcode.com）
    UI_HEADLESS         — 是否无头模式（默认 true）
    UI_VIEWPORT_W       — 视口宽度（默认 1280）
    UI_VIEWPORT_H       — 视口高度（默认 720）
    GITCODE_UI_COOKIE   — cookie JSON 文件路径（可选，用于登录态注入）
"""
import os
import sys
import json
import time
import yaml

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout


HERE = os.path.dirname(os.path.abspath(__file__))


class UiConfig:
    """UI 执行器配置。"""

    def __init__(self, owner=None, repo=None, base_url=None,
                 headless=None, viewport=None):
        self.owner = owner or os.environ.get("GITCODE_OWNER", "weixin_55883847")
        self.repo = repo or os.environ.get("GITCODE_REPO", "gitcode_api")
        self.base_url = (base_url or os.environ.get(
            "GITCODE_UI_BASE_URL", "https://gitcode.com"
        )).rstrip("/")
        self.headless = headless if headless is not None else (
            os.environ.get("UI_HEADLESS", "true").lower() in ("1", "true", "yes")
        )
        self.viewport = viewport or {
            "width": int(os.environ.get("UI_VIEWPORT_W", "1280")),
            "height": int(os.environ.get("UI_VIEWPORT_H", "720")),
        }


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] [UI] {msg}", flush=True)


def _resolve_url(url, cfg):
    """替换 URL 中的 {owner}/{repo} 占位符，并补全相对路径。"""
    if url.startswith("/"):
        url = cfg.base_url + url
    return url.replace("{owner}", cfg.owner).replace("{repo}", cfg.repo)


def _resolve_vars(text, cfg):
    """替换任意字符串中的 {owner}/{repo} 占位符。"""
    if not isinstance(text, str):
        return text
    return text.replace("{owner}", cfg.owner).replace("{repo}", cfg.repo)


def _load_cookies(cookie_path):
    """从 JSON 文件加载 cookie 列表。"""
    if not cookie_path or not os.path.exists(cookie_path):
        return []
    with open(cookie_path, encoding="utf-8") as f:
        data = json.load(f)
    # 支持两种格式: [{name, value, domain, path}] 或 {"name": "value"}
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return [
            {"name": k, "value": v, "domain": ".gitcode.com", "path": "/"}
            for k, v in data.items()
        ]
    return []


def _apply_actions(page, actions, cfg):
    """在页面上执行 action 序列。"""
    for action in (actions or []):
        atype = action.get("type")
        log(f"  action: {atype}")

        if atype == "navigate":
            url = _resolve_url(action["url"], cfg)
            wait_until = action.get("wait_until", "networkidle")
            page.goto(url, wait_until=wait_until)

        elif atype == "click":
            selector = _resolve_vars(action["selector"], cfg)
            page.click(selector, timeout=action.get("timeout", 10000))

        elif atype == "fill":
            selector = _resolve_vars(action["selector"], cfg)
            value = _resolve_vars(action["value"], cfg)
            page.locator(selector).first.fill(value)

        elif atype == "type":
            selector = _resolve_vars(action["selector"], cfg)
            value = _resolve_vars(action["value"], cfg)
            page.locator(selector).first.type(value)

        elif atype == "select":
            selector = _resolve_vars(action["selector"], cfg)
            value = _resolve_vars(action["value"], cfg)
            page.select_option(selector, value)

        elif atype == "screenshot":
            path = _resolve_vars(action.get("path", "screenshot.png"), cfg)
            page.screenshot(path=path, full_page=action.get("full_page", False))
            log(f"  screenshot saved: {path}")

        elif atype == "wait":
            ms = action.get("ms", 1000)
            page.wait_for_timeout(ms)

        elif atype == "wait_for_selector":
            selector = _resolve_vars(action["selector"], cfg)
            page.wait_for_selector(selector, timeout=action.get("timeout", 10000))

        else:
            log(f"  WARN: unknown action type '{atype}'")

        # action 间默认短暂等待，避免动画未结束
        time.sleep(action.get("wait", 0.3))


def _evaluate_assertions(page, assertions, cfg):
    """评估断言列表。"""
    results = []
    for assertion in (assertions or []):
        atype = assertion.get("type", "positive")
        target = assertion["target"]
        passed = False
        detail = ""

        try:
            if target == "ui_element_visible":
                selector = _resolve_vars(assertion["selector"], cfg)
                timeout = assertion.get("timeout", 5000)
                page.wait_for_selector(selector, timeout=timeout, state="visible")
                passed = True
                detail = f"Element visible: {selector}"

            elif target == "ui_text_contains":
                selector = _resolve_vars(assertion.get("selector", "body"), cfg)
                text = _resolve_vars(assertion["text"], cfg)
                if selector == "title":
                    raw = page.title()
                else:
                    locator = page.locator(selector)
                    raw = locator.inner_text(timeout=assertion.get("timeout", 5000))
                passed = text in raw
                detail = f"Text '{text}' {'found' if passed else 'NOT found'} in {selector}"

            elif target == "ui_page_title":
                expected = _resolve_vars(assertion["text"], cfg)
                actual = page.title()
                passed = expected in actual
                detail = f"Page title '{actual}' {'contains' if passed else 'does NOT contain'} '{expected}'"

            elif target == "ui_url_match":
                expected = _resolve_vars(assertion["expected"], cfg)
                actual = page.url
                passed = expected in actual
                detail = f"URL '{actual}' {'matches' if passed else 'does NOT match'} '{expected}'"

            elif target == "ui_element_count":
                selector = _resolve_vars(assertion["selector"], cfg)
                expected = assertion["expected_count"]
                count = page.locator(selector).count()
                passed = count == expected
                detail = f"Element count {count} {'==' if passed else '!='} {expected}"

            else:
                detail = f"Unknown assertion target: {target}"
        except PlaywrightTimeout:
            passed = False
            detail = f"Timeout waiting for assertion: {target}"
        except Exception as e:
            passed = False
            detail = f"Exception: {e}"

        results.append({
            "assertion": target,
            "type": atype,
            "passed": passed,
            "detail": detail,
        })
    return results


def run_ui_case(cfg, case_id, url, actions=None, assertions=None,
                cookies=None, output_dir=None):
    """
    执行单条 UI 测试用例。
    返回 dict（结构同 api_runner 的 RunResult，供统一报告消费）。
    """
    t0 = time.time()
    log(f"=== UI {case_id} → {url} ===")

    result = {
        "case_id": case_id,
        "status": "COMPLETED",
        "ui_url": url,
        "duration_seconds": 0,
        "assertions": [],
        "screenshots": [],
        "logs": "",
        "logs_available": True,
    }

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=cfg.headless)
            context = browser.new_context(viewport=cfg.viewport)

            # 注入 cookie（登录态）
            if cookies:
                context.add_cookies(cookies)

            page = context.new_page()

            # 1. 初始导航
            resolved_url = _resolve_url(url, cfg)
            page.goto(resolved_url, wait_until="networkidle")
            log(f"  navigated to {page.url}")

            # 2. 执行 actions
            _apply_actions(page, actions or [], cfg)

            # 3. 断言评估
            result["assertions"] = _evaluate_assertions(page, assertions or [], cfg)
            all_pass = all(a["passed"] for a in result["assertions"])
            result["status"] = "PASS" if all_pass else "FAIL"

            # 4. 最终截图（用于调试/报告）
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                final_shot = os.path.join(output_dir, f"{case_id}_final.png")
            else:
                final_shot = f"{case_id}_final.png"
            page.screenshot(path=final_shot, full_page=True)
            result["screenshots"].append(final_shot)

            browser.close()

    except Exception as e:
        log(f"  → ENV_ERROR: {e}")
        result["status"] = "ENV_ERROR"
        result["error"] = str(e)

    result["duration_seconds"] = round(time.time() - t0, 2)
    log(f"  ← {result['status']} ({result['duration_seconds']}s)")
    return result


def main():
    if len(sys.argv) < 2:
        print("usage: ui_runner.py <case-yaml> [output-log.txt]")
        sys.exit(2)

    yaml_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None

    with open(yaml_path, encoding="utf-8") as f:
        case = yaml.safe_load(f)

    cfg = UiConfig()
    cookies = _load_cookies(os.environ.get("GITCODE_UI_COOKIE"))

    result = run_ui_case(
        cfg=cfg,
        case_id=case.get("id", "UNKNOWN"),
        url=case["ui"]["url"],
        actions=case["ui"].get("actions", []),
        assertions=case.get("assertions", []),
        cookies=cookies,
        output_dir=os.path.dirname(out_path) if out_path else None,
    )

    # 输出日志
    log_text = json.dumps(result, ensure_ascii=False, indent=2)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(log_text)
    else:
        print(log_text)

    # 返回码: 0=PASS, 1=FAIL, 2=ENV_ERROR
    if result["status"] == "PASS":
        sys.exit(0)
    elif result["status"] == "FAIL":
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ui_runner self-check: imports OK")
        try:
            cfg = UiConfig()
            print(f"  config: {cfg.owner}/{cfg.repo} ui={cfg.base_url} headless={cfg.headless} viewport={cfg.viewport}")
        except Exception as e:
            print(f"  config load: {type(e).__name__}: {e}")
        sys.exit(0)
    main()
