#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_batch.py — Phase 02 批量执行器（确定性；slash 命令与 CI 共用入口）

读 queue.json，逐条调 run_case.py 真跑。**每条前后更新 state.json**，使 status.py
可在执行中途读到进度（done/total/current）。编译产物（compiled/）由上游 yaml-checker
产出——本脚本不编译；缺编译产物的用例 run_case 会判 NOT_CONFIGURED。

用法:
  python run_batch.py <phase02-run-id> [--no-logs] [--only c1,c2]
  例: python run_batch.py 2026-07-21-10

CI 友好：不依赖 Claude，消费已入库的 compiled/ 产物即可 headless 运行。
"""
import os
import sys
import json
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PHASE02 = os.path.dirname(HERE)
ROOT = os.path.dirname(PHASE02)

sys.path.insert(0, HERE)
import workflow_runner as wr
import assertion_engine as ae
import run_case as rc


def _load(path, default=None):
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else default


def _write_state(run_dir, state):
    json.dump(state, open(os.path.join(run_dir, "state.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


def _update_run_md(run_dir, run_id, state):
    with open(os.path.join(run_dir, "run.md"), "w", encoding="utf-8") as f:
        f.write(f"# Phase 02 Run {run_id}\n\n")
        f.write(f"- 状态: {state['status']}\n")
        f.write(f"- 进度: {state['done']}/{state['total']}"
                + (f"（当前: {state['current']}）" if state.get("current") else "") + "\n")
        v = state.get("verdicts", {})
        if v:
            f.write("- 判定累计: " + " · ".join(f"{k}={n}" for k, n in v.items()) + "\n")


def main():
    if len(sys.argv) < 2:
        print("usage: run_batch.py <phase02-run-id> [--no-logs] [--only c1,c2]")
        sys.exit(2)
    run_id = sys.argv[1]
    args = sys.argv[2:]
    no_logs = "--no-logs" in args
    only = None
    if "--only" in args:
        only = set(args[args.index("--only") + 1].split(","))

    run_dir = os.path.join(PHASE02, "runs", run_id)
    queue = _load(os.path.join(run_dir, "queue.json"))
    if not queue:
        print(f"缺 queue.json（先跑 schema_check.py）: runs/{run_id}/")
        sys.exit(1)
    cases = [c for c in queue["cases"] if not only or c["case_id"] in only]

    state = {"status": "running", "total": len(cases), "done": 0,
             "current": None, "verdicts": {}, "started": time.strftime("%H:%M:%S")}
    _write_state(run_dir, state)
    _update_run_md(run_dir, run_id, state)
    print(f"=== 批量执行 {run_id} · {len(cases)} 条 ===")

    for i, c in enumerate(cases, 1):
        cid = c["case_id"]
        contract_path = os.path.join(ROOT, c["contract_path"])
        state["current"] = f"{cid} ({i}/{len(cases)})"
        _write_state(run_dir, state)
        _update_run_md(run_dir, run_id, state)
        print(f"[{i}/{len(cases)}] {cid} ...")

        contract_doc = rc.load_contract(contract_path)
        test_type = contract_doc.get("test_type", "workflow")

        try:
            if test_type == "workflow":
                cfg = wr.RunnerConfig(branch=None)
                ok, verr = wr.preflight_validate(contract_doc, cfg=cfg)
                if not ok:
                    wr.log(f"{cid}: 预检不通过（{len(verr)} 项）→ COMPILE_ERROR，不 push")
                    for e in verr:
                        wr.log(f"    - {e}")
                    verdict = {"verdict": "COMPILE_ERROR", "verdict_flags": [],
                               "reason": "; ".join(verr), "assertion_results": []}
                    rr = {"status": "COMPILE_ERROR", "case_id": cid}
                else:
                    wf, asserts = rc.load_execution_inputs(contract_doc, run_dir, cid)
                    if not wf:
                        wr.log(f"{cid}: 契约无 workflow 字段 → NOT_CONFIGURED")
                        verdict = {"verdict": "NOT_CONFIGURED", "verdict_flags": [],
                                   "reason": "Phase 01 契约无 workflow 字段", "assertion_results": []}
                        rr = {"status": "NOT_CONFIGURED", "case_id": cid}
                    else:
                        ev = (contract_doc.get("trigger") or {}).get("event", "push")
                        trig_as = (contract_doc.get("trigger") or {}).get("as", "maintainer")
                        if trig_as == "untrusted_contributor":
                            cp = os.path.expanduser("~/.gitcode-contributor-token")
                            if ev in ("issue_comment", "pull_request_comment") and os.path.exists(cp):
                                pass
                            else:
                                wr.log(f"{cid}: trigger.as=untrusted_contributor → INCONCLUSIVE")
                                verdict = {"verdict": "INCONCLUSIVE", "verdict_flags": [],
                                           "reason": "untrusted_contributor 执行路径未实现，拒绝以 maintainer 假验证",
                                           "assertion_results": []}
                                rr = {"status": "INCONCLUSIVE", "case_id": cid}
                        else:
                            verdict, rr = rc.run_workflow_case(contract_doc, run_dir, cid, cfg, fetch_logs=not no_logs)

            elif test_type == "api":
                verdict, rr = rc.run_api_case(contract_doc, cid)

            elif test_type == "git":
                verdict, rr = rc.run_git_case(contract_doc, cid)

            else:
                verdict = {"verdict": "COMPILE_ERROR", "verdict_flags": [],
                           "reason": f"未知 test_type: {test_type}", "assertion_results": []}
                rr = {"status": "COMPILE_ERROR", "case_id": cid}

        except Exception as e:
            wr.log(f"{cid}: 异常 → ENV_ERROR: {e}")
            verdict = {"verdict": "ENV_ERROR", "verdict_flags": [],
                       "reason": str(e), "assertion_results": []}
            rr = {"status": "ENV_ERROR", "case_id": cid, "reason": str(e)}

        rec = rc.write_result(run_dir, contract_doc, verdict, rr)
        rc.update_summary(run_dir, rec)
        v = rec["verdict"]
        wr.log(f"  → {v} ({rec['duration_seconds']}s)")

        state["verdicts"][v] = state["verdicts"].get(v, 0) + 1
        state["done"] = i
        state["current"] = None
        _write_state(run_dir, state)
        _update_run_md(run_dir, run_id, state)

    state["status"] = "completed"
    _write_state(run_dir, state)
    _update_run_md(run_dir, run_id, state)
    print(f"=== 完成 · " + " · ".join(f"{k}={n}" for k, n in state["verdicts"].items()) + " ===")


if __name__ == "__main__":
    main()
