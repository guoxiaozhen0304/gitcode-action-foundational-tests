#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_project.py — 动态创建测试项目并初始化资源

用法:
    python setup_project.py [owner]

产出:
    project_state.json — 包含 owner/repo/branches/issue_number/hook_id/milestone_title
"""
import os
import sys
import json
import time
import urllib.request
import urllib.error

TOKEN = open(os.path.expanduser('~/.gitcode-token'), encoding='utf-8').read().strip()
OWNER = sys.argv[1] if len(sys.argv) > 1 else 'weixin_55883847'
TS = str(int(time.time()))
REPO_NAME = f'gitcode_test_run_{TS}'


def api_call(method, endpoint, params=None, content_type='application/json'):
    url = f'https://gitcode.com{endpoint}'
    data = None
    if method in ('POST', 'PUT', 'PATCH') and params:
        if content_type == 'application/x-www-form-urlencoded':
            data = urllib.parse.urlencode(params).encode('utf-8')
        else:
            data = json.dumps(params).encode('utf-8')

    headers = {'Authorization': f'Bearer {TOKEN}'}
    if data:
        headers['Content-Type'] = content_type

    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode('utf-8', errors='replace')
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace') if e.fp else '{}'
        try:
            return json.loads(body)
        except Exception:
            return {'_error': body, '_status': e.code}
    except Exception as e:
        return {'_error': str(e), '_status': 0}


def log(msg):
    print(f'[setup] {msg}', flush=True)


def main():
    log(f'Creating project {REPO_NAME}...')
    repo = api_call('POST', '/api/v5/user/repos', {
        'name': REPO_NAME,
        'description': 'Auto-created by Phase02 runner',
        'private': False,
        'auto_init': True
    })
    if '_error' in repo and '_status' in repo:
        log(f'FAIL create repo: {repo}')
        sys.exit(1)
    log(f'Created: {repo.get("full_name", REPO_NAME)}')

    # 等待项目就绪
    time.sleep(2)

    # 创建分支
    branches = []
    for b in [f'feature-branch-{TS}', f'wip-branch-{TS}']:
        log(f'Creating branch {b}...')
        r = api_call('POST', f'/api/v5/repos/{OWNER}/{REPO_NAME}/branches',
                     {'branch_name': b, 'refs': 'main'})
        if r.get('name') == b:
            branches.append(b)
            log(f'  OK')
        else:
            log(f'  WARN: {r}')

    # 创建 Issue
    log('Creating Issue...')
    issue = api_call('POST', f'/api/v5/repos/{OWNER}/{REPO_NAME}/issues',
                     {'title': 'Fixture Issue', 'body': 'Fixture'},
                     content_type='application/x-www-form-urlencoded')
    issue_number = issue.get('number', '1')
    log(f'  Issue number: {issue_number}')

    # 创建 Hook
    log('Creating Hook...')
    hook = api_call('POST', f'/api/v5/repos/{OWNER}/{REPO_NAME}/hooks',
                    {'url': 'https://example.com/webhook', 'push_events': 'true'},
                    content_type='application/x-www-form-urlencoded')
    hook_id = hook.get('id')
    log(f'  Hook id: {hook_id}')

    # 创建 Milestone
    log('Creating Milestone...')
    ms_title = f'v1.0.0-{TS}'
    ms = api_call('POST', f'/api/v5/repos/{OWNER}/{REPO_NAME}/milestones',
                  {'title': ms_title, 'description': 'Fixture'},
                  content_type='application/x-www-form-urlencoded')
    milestone_title = ms.get('title', ms_title)
    log(f'  Milestone title: {milestone_title}')

    state = {
        'owner': OWNER,
        'repo': REPO_NAME,
        'timestamp': TS,
        'branches': branches,
        'issue_number': str(issue_number),
        'hook_id': hook_id,
        'milestone_title': milestone_title,
    }

    with open('project_state.json', 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    log('project_state.json written.')
    log(f'Ready: {OWNER}/{REPO_NAME}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
