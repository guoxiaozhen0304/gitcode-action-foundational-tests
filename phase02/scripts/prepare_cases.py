#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prepare_cases.py — 根据 project_state.json 批量替换 YAML 中的动态资源名

用法:
    python prepare_cases.py <src-dir> <dst-dir> <state-json>

替换规则:
    - repo_fixture → owner/repo
    - feature-branch / wip-branch / test-branch-api-004-v2 → 动态分支名
    - /issues/1/ → /issues/{issue_number}/
    - /hooks/73280/ /hooks/73475/ /hooks/73043/ → /hooks/{hook_id}/
    - tag / milestone 版本号 → 带时间戳的版本
    - /pulls/2/ → /pulls/1/（新仓库第一个 MR 编号为 1）
"""
import os
import sys
import json
import shutil


def main():
    if len(sys.argv) < 4:
        print("usage: prepare_cases.py <src-dir> <dst-dir> <state-json>")
        sys.exit(2)

    src_dir, dst_dir, state_path = sys.argv[1], sys.argv[2], sys.argv[3]
    state = json.load(open(state_path, encoding='utf-8'))

    os.makedirs(dst_dir, exist_ok=True)

    repo_ref = f"{state['owner']}/{state['repo']}"
    ts = state['timestamp']
    branches = state['branches']
    issue_number = state['issue_number']
    hook_id = state['hook_id']

    replacements = {
        # repo fixture
        'weixin_55883847/gitcode_apitest': repo_ref,
        'openeuler-test/gitcode_apitest': repo_ref,
        'ComputingActionTest/gitcode_api': repo_ref,
        # branches
        'feature-branch': branches[0] if len(branches) > 0 else f'feature-branch-{ts}',
        'wip-branch': branches[1] if len(branches) > 1 else f'wip-branch-{ts}',
        'test-branch-api-004': f'test-branch-api-004-{ts}',
        # issue / hook
        '/issues/1/': f'/issues/{issue_number}/',
        '/hooks/73280/': f'/hooks/{hook_id}/',
        '/hooks/73475/': f'/hooks/{hook_id}/',
        '/hooks/73043/': f'/hooks/{hook_id}/',
        # versions
        'v1.0.3': f'v1.0.{ts}',
        'v1.0.2': f'v1.0.{ts}',
        'v1.0.1': f'v1.0.{ts}',
        'v4.0.0': f'v4.0.0-{ts}',
        'v3.0.0': f'v3.0.0-{ts}',
        'v2.0.0': f'v2.0.0-{ts}',
        # MR number (new repo starts from 1)
        '/pulls/2/': '/pulls/1/',
        # delete project endpoint in API-REPO-01-005
        '/api/v5/repos/{owner}/gitcode_test_run': f'/api/v5/repos/{repo_ref}',
    }

    copied = 0
    for fname in sorted(os.listdir(src_dir)):
        if not fname.endswith(('.yaml', '.yml')):
            continue
        src_path = os.path.join(src_dir, fname)
        dst_path = os.path.join(dst_dir, fname)
        with open(src_path, encoding='utf-8') as f:
            content = f.read()
        for old, new in replacements.items():
            content = content.replace(old, new)

        # 特殊处理：API-SMOKE-01-069 会真实删除仓库，改指向不存在的仓库
        if fname == 'API-SMOKE-01-069.yaml':
            content = content.replace(
                'endpoint: /api/v5/repos/{owner}/{repo}',
                'endpoint: /api/v5/repos/{owner}/nonexistent-repo'
            )

        # 特殊处理：API-REPO-01-004 中硬编码的旧项目名
        if fname == 'API-REPO-01-004.yaml':
            content = content.replace(
                '"name": "gitcode_test_run"',
                f'"name": "{state["repo"]}"'
            )

        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(content)
        copied += 1

    print(f'Prepared {copied} cases → {dst_dir}')
    print(f'  repo: {repo_ref}')
    print(f'  branches: {branches}')
    print(f'  issue: {issue_number}, hook: {hook_id}')


if __name__ == '__main__':
    main()
