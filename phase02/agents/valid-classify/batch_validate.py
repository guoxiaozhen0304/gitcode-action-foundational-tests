#!/usr/bin/env python3
"""批量校验 case YAML 并按结果分组到 VALID / INVALID / ERROR_WAF / SKIP。

用法:
    python3 batch_validate.py <cases-yaml-dir> <output-dir>
    python3 batch_validate.py phase01/runs/2026-07-23-01/cases/yaml/ phase02/classify-experiment/2026-07-23/

认证: 从项目根目录 .env 读取 GITCODE_COOKIE。
"""
import base64
import json
import os
import shutil
import sys
import time
from pathlib import Path

import requests
import yaml

DEFAULT_WF_ID = "b03a4b84cd784ddea00c5270eba62c7f"
API_HOST = "web-api.gitcode.com"
PROJECT = "ComputingActionTest/foundational-tests"
SLEEP = 0.8  # 每个请求间隔秒

WAF_WHITELIST = {
    "COMP-ATOMGIT-01-047", "COMP-ATOMGIT-01-048", "COMP-ATOMGIT-01-049",
    "COMP-SCRIPT-01-082",
    "COMPAT-TOKEN-01-001", "COMPAT-TOKEN-01-002",
    "REL-LOG-01-040", "REL-OUTPUT-01-017",
    "USE-MASK-01-001", "SEC-NAME-01-002", "SEC-ENV-WAIT-02-001",
}


def load_env():
    root = Path(__file__).resolve().parent
    for _ in range(4):
        envf = root / ".env"
        if envf.exists():
            break
        root = root.parent
    env = {}
    if root and (root / ".env").exists():
        with open(root / ".env") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, _, v = line.partition("=")
                    env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def validate_workflow(file_content: str, cookie: str, workflow_id: str, file_path: str) -> dict:
    encoded_project = PROJECT.replace("/", "%2F")
    url = f"https://{API_HOST}/api/v2/projects/{encoded_project}/actions/valid"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cookie}",
        "Origin": "https://gitcode.com",
        "Referer": "https://gitcode.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        "X-App-Channel": "gitcode-fe",
        "X-App-Version": "0",
        "X-Device-ID": "unknown",
        "X-Device-Type": "Linux",
        "X-Platform": "web",
        "Cookie": f"GITCODE_ACCESS_TOKEN={cookie}; GitCodeUserName=ccijunk",
    }
    encoded_content = base64.b64encode(file_content.encode("utf-8")).decode("utf-8")
    payload = {"workflow_id": workflow_id, "file_path": file_path, "file_content": encoded_content}
    try:
        resp = requests.post(url, params={"workflow_id": workflow_id}, headers=headers, json=payload, timeout=15)
        if "application/json" in resp.headers.get("Content-Type", ""):
            return resp.json()
        return {"status_code": resp.status_code, "text": resp.text}
    except requests.RequestException as e:
        return {"error": str(e)}


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <cases-yaml-dir> <output-dir>")
        sys.exit(1)

    src_dir = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    valid_dir = out_dir / "valid"
    invalid_dir = out_dir / "invalid"
    waf_dir = out_dir / "WAF"
    skip_dir = out_dir / "SKIP"
    for d in [valid_dir, invalid_dir, waf_dir, skip_dir]:
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    # Also clean legacy uppercase dirs
    for d in [out_dir / "VALID", out_dir / "INVALID", out_dir / "ERROR_WAF"]:
        if d.exists():
            shutil.rmtree(d)

    cookie = os.environ.get("GITCODE_COOKIE") or load_env().get("GITCODE_COOKIE", "")
    if not cookie:
        print("FATAL: GITCODE_COOKIE not found in env or .env"); sys.exit(1)

    yaml_files = sorted(src_dir.glob("*.yaml"))
    results = []
    counts = {"VALID": 0, "INVALID": 0, "WAF": 0, "SKIP": 0}

    for i, yf in enumerate(yaml_files, 1):
        cid = yf.stem
        with open(yf) as f:
            case = yaml.safe_load(f)
        wf_text = case.get("workflow", "")

        if not wf_text:
            shutil.copy2(str(yf), str(skip_dir / yf.name))
            counts["SKIP"] += 1
            print(f"[{i:>3}/{len(yaml_files)}] {cid}  SKIP (no workflow)")
            results.append({"case_id": cid, "status": "SKIP", "diagnostics": []})
            continue

        wf_name = cid.lower().replace("_", "-") + ".yml"
        file_path = f".gitcode/workflows/{wf_name}"

        resp = validate_workflow(wf_text, cookie, DEFAULT_WF_ID, file_path)
        valid = resp.get("valid")
        status_code = resp.get("status_code")

        if valid is True:
            shutil.copy2(str(yf), str(valid_dir / yf.name))
            r = {"case_id": cid, "status": "VALID", "diagnostics": []}
            counts["VALID"] += 1
        elif valid is False:
            shutil.copy2(str(yf), str(invalid_dir / yf.name))
            diags = []
            for d in resp.get("diagnostics", []):
                diags.append({
                    "severity": d.get("severity", "?"),
                    "message": d.get("message", ""),
                    "line": d.get("range", {}).get("start", {}).get("line", "?"),
                    "column": d.get("range", {}).get("start", {}).get("column", "?"),
                })
            r = {"case_id": cid, "status": "INVALID", "diagnostics": diags}
            counts["INVALID"] += 1
        elif status_code == 418:
            if cid in WAF_WHITELIST:
                shutil.copy2(str(yf), str(valid_dir / yf.name))
                r = {"case_id": cid, "status": "VALID", "via": "WAF_WHITELIST", "diagnostics": [], "http_status": 418}
                counts["VALID"] += 1
            else:
                shutil.copy2(str(yf), str(waf_dir / yf.name))
                r = {"case_id": cid, "status": "WAF", "diagnostics": [], "http_status": 418}
                counts["WAF"] += 1
        else:
            r = {"case_id": cid, "status": "ERROR", "diagnostics": [], "raw": json.dumps(resp, ensure_ascii=False)[:300]}
            counts["WAF"] += 1
            shutil.copy2(str(yf), str(waf_dir / yf.name))

        results.append(r)
        n_diag = len(r.get("diagnostics", []))
        tag = r["status"]
        extra = f" ({n_diag} diag)" if n_diag else ""
        if r.get("via") == "WAF_WHITELIST":
            extra = " (WAF whitelist)"
        elif tag == "WAF":
            extra = " (WAF 418)"
        print(f"[{i:>3}/{len(yaml_files)}] {cid}  {tag}{extra}")
        sys.stdout.flush()
        time.sleep(SLEEP)

    # Save results JSON
    with open(out_dir / "validation-results.json", "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nDone: {len(yaml_files)} cases")
    print(f"  valid:     {counts['VALID']}")
    print(f"  invalid:   {counts['INVALID']}")
    print(f"  WAF:       {counts['WAF']}")
    print(f"  SKIP:      {counts['SKIP']}")
    print(f"Results: {out_dir / 'validation-results.json'}")


if __name__ == "__main__":
    main()
