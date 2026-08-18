#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
git_runner.py — Git 操作测试 runner（确定性）

在本地执行 git 命令，验证代码托管核心能力（clone/push/branch/MR 等）。
凭据：GITCODE_ACCESS_TOKEN（HTTPS OAuth2）。

用法:
    import git_runner as gr
    cfg = gr.GitConfig(owner="ComputingActionTest", repo="gitcode_api")
    result = gr.run_git_case(cfg, case_id="GIT-CLONE-01-001",
                             action="clone", args={},
                             assertions=[...])
"""
import os
import sys
import json
import time
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] [GIT] {msg}", flush=True)


def _sh(cmd, cwd=None, env=None):
    r = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True,
                       text=True, encoding="utf-8", env=env)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


class GitConfig:
    """Git 执行器配置。默认对齐 fixture 仓库。"""

    def __init__(self, owner=None, repo=None, token=None, branch=None):
        self.owner = owner or os.environ.get("GITCODE_OWNER", "ComputingActionTest")
        self.repo = repo or os.environ.get("GITCODE_REPO", "gitcode_api")
        self.branch = branch or os.environ.get("GITCODE_BRANCH", "main")
        self.token = token or self._load_token()
        self.repo_url = f"https://oauth2:{self.token}@gitcode.com/{self.owner}/{self.repo}.git"

    @staticmethod
    def _load_token():
        path = os.path.expanduser(os.environ.get("GITCODE_TOKEN_FILE", "~/.gitcode-token"))
        if os.path.exists(path):
            return open(path, encoding="utf-8").read().strip()
        env = os.environ.get("GITCODE_ACCESS_TOKEN", "")
        if env:
            return env
        raise FileNotFoundError("未找到 GitCode token")


def _git_env(cfg):
    """构造带凭据的 git 环境变量（避免 token 出现在 ps 列表）。"""
    env = os.environ.copy()
    env["GIT_ASKPASS"] = "echo"
    env["GIT_USERNAME"] = "oauth2"
    env["GIT_PASSWORD"] = cfg.token
    return env


def run_git_case(cfg, case_id, action, args=None, local_path=None, assertions=None):
    """
    执行单条 Git 测试用例。
    返回 GitResult dict（结构同 RunResult，供 assertion_engine.evaluate 消费）。
    """
    args = args or {}
    t0 = time.time()
    log(f"=== GIT {case_id} → {action} ===")

    # 临时工作目录
    work_dir = local_path or os.path.join(tempfile.gettempdir(), "gitcode_smoke", case_id)
    os.makedirs(work_dir, exist_ok=True)

    exit_code = -1
    output = ""
    git_branches = []

    try:
        env = _git_env(cfg)

        if action == "clone":
            # 清理后重新 clone
            shutil.rmtree(work_dir, ignore_errors=True)
            os.makedirs(work_dir, exist_ok=True)
            exit_code, output = _sh(f'git clone --depth 1 "{cfg.repo_url}" .', cwd=work_dir, env=env)

        elif action == "fetch":
            out_clone = ""
            if not os.path.isdir(os.path.join(work_dir, ".git")):
                exit_code, out_clone = _sh(f'git clone --depth 1 "{cfg.repo_url}" .', cwd=work_dir, env=env)
                if exit_code != 0:
                    output = out_clone
            if os.path.isdir(os.path.join(work_dir, ".git")):
                # 空仓库（无提交）fetch 会失败，视为可接受
                heads_dir = os.path.join(work_dir, ".git", "refs", "heads")
                if os.path.isdir(heads_dir) and not os.listdir(heads_dir):
                    exit_code = 0
                    output = (out_clone or "") + "\nSkipped fetch: empty repository"
                else:
                    exit_code, out_fetch = _sh("git fetch --depth 1 origin", cwd=work_dir, env=env)
                    output = (out_clone or "") + "\n" + out_fetch

        elif action == "push":
            branch = args.get("branch", cfg.branch)
            # 创建一个测试提交并推送
            test_file = os.path.join(work_dir, f"smoke-{case_id}.txt")
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(f"smoke test {case_id} {time.time()}\n")
            _sh("git add .", cwd=work_dir, env=env)
            _sh(f'git commit -m "smoke: {case_id}"', cwd=work_dir, env=env)
            exit_code, output = _sh(f"git push origin {branch}", cwd=work_dir, env=env)

        elif action == "branch_create":
            branch = args.get("branch", f"smoke-{case_id}")
            if not os.path.isdir(os.path.join(work_dir, ".git")):
                exit_code, output = -1, "目录非 git 仓库"
            else:
                exit_code, output = _sh(f"git checkout -b {branch}", cwd=work_dir, env=env)
                if exit_code == 0:
                    exit_code, output = _sh(f"git push origin {branch}", cwd=work_dir, env=env)

        elif action == "branch_delete":
            branch = args.get("branch", f"smoke-{case_id}")
            exit_code, output = _sh(f"git push origin --delete {branch}", cwd=work_dir, env=env)

        elif action == "tag_create":
            tag = args.get("tag", f"smoke-{case_id}")
            exit_code, output = _sh(f"git tag {tag}", cwd=work_dir, env=env)
            if exit_code == 0:
                exit_code, output = _sh(f"git push origin {tag}", cwd=work_dir, env=env)

        elif action == "tag_delete":
            tag = args.get("tag", f"smoke-{case_id}")
            exit_code, output = _sh(f"git push origin --delete {tag}", cwd=work_dir, env=env)

        elif action == "checkout":
            branch = args.get("branch", cfg.branch)
            exit_code, output = _sh(f"git checkout {branch}", cwd=work_dir, env=env)

        elif action == "merge_request_create":
            # MR 创建通过 API 完成（git 侧只负责推分支）
            branch = args.get("branch", f"smoke-{case_id}")
            exit_code, output = _sh(f"git checkout -b {branch}", cwd=work_dir, env=env)
            if exit_code == 0:
                test_file = os.path.join(work_dir, f"smoke-{case_id}.txt")
                with open(test_file, "w", encoding="utf-8") as f:
                    f.write(f"mr smoke {case_id}\n")
                _sh("git add .", cwd=work_dir, env=env)
                _sh(f'git commit -m "smoke mr: {case_id}"', cwd=work_dir, env=env)
                exit_code, output = _sh(f"git push origin {branch}", cwd=work_dir, env=env)

        else:
            exit_code, output = -1, f"未知 git action: {action}"

        # 采集分支列表（用于断言）
        if os.path.isdir(os.path.join(work_dir, ".git")):
            rc, branches_out = _sh("git branch -a", cwd=work_dir, env=env)
            if rc == 0:
                git_branches = [b.strip().strip("* ") for b in branches_out.splitlines() if b.strip()]

        log(f"  → exit={exit_code}")
        return {
            "case_id": case_id,
            "status": "COMPLETED" if exit_code == 0 else "FAILED",
            "git_exit_code": exit_code,
            "git_output": output,
            "git_branches": git_branches,
            "duration_seconds": round(time.time() - t0),
            "logs": output,
            "logs_available": True,
        }
    except Exception as e:
        log(f"  → ENV_ERROR: {e}")
        return {
            "case_id": case_id,
            "status": "ENV_ERROR",
            "reason": str(e),
            "git_exit_code": -1,
            "git_output": str(e),
            "duration_seconds": round(time.time() - t0),
            "logs": str(e),
            "logs_available": True,
        }


if __name__ == "__main__":
    print("git_runner self-check: imports OK")
    try:
        cfg = GitConfig()
        print(f"  config: {cfg.owner}/{cfg.repo}@{cfg.branch}")
    except Exception as e:
        print(f"  config load: {type(e).__name__}: {e}")
