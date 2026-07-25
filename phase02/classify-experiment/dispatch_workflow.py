#!/usr/bin/env python3
"""Dispatch a GitCode workflow via v2 API, return the run_id."""
import requests, json, sys, os

cookie = os.environ.get('GITCODE_COOKIE', '')
owner = os.environ.get('GITCODE_OWNER', 'ComputingActionTest')
repo = os.environ.get('GITCODE_REPO', 'foundational-tests')
branch = os.environ.get('GITCODE_BRANCH', 'main')
executor = os.environ.get('GITCODE_EXECUTOR', 'ccijunk')
wf_path = sys.argv[1] if len(sys.argv) > 1 else ''

if not cookie:
    print('ERROR: GITCODE_COOKIE not set')
    sys.exit(1)
if not wf_path:
    print('ERROR: workflow file_path required')
    sys.exit(1)

project = f'{owner}%2F{repo}'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {cookie}',
    'Origin': 'https://gitcode.com',
    'Referer': 'https://gitcode.com/',
    'User-Agent': 'Mozilla/5.0',
    'Cookie': f'GITCODE_ACCESS_TOKEN={cookie}; GitCodeUserName={executor}',
}

# List workflows
r = requests.post(f'https://web-api.gitcode.com/api/v2/projects/{project}/actions/workflows/list',
    headers=headers, json={'per_page': 50}, timeout=10)
if r.status_code != 200:
    print(f'ERROR: list API returned {r.status_code}: {r.text[:200]}')
    sys.exit(1)

wfs = r.json().get('content', [])
wf_id = None
for w in wfs:
    if w.get('file_path', '') == wf_path:
        wf_id = w['workflow_id']
        break

if not wf_id:
    # Try matching by suffix
    for w in wfs:
        if w.get('file_path', '').endswith(wf_path) or wf_path.endswith(w.get('file_path', '')):
            wf_id = w['workflow_id']
            break

if not wf_id:
    print(f'ERROR: workflow {wf_path} not found in list ({len(wfs)} workflows)')
    sys.exit(1)

# Dispatch
payload = {
    'ref': branch, 'branch': branch, 'branch_commit_id': '',
    'repo_https_url': f'https://gitcode.com/{owner}/{repo}.git',
    'file_path': wf_path, 'inputs': {},
}
rd = requests.post(
    f'https://web-api.gitcode.com/api/v2/projects/{project}/actions/workflows/{wf_id}/dispatch',
    headers=headers, json=payload, timeout=10)

if rd.status_code != 200:
    print(f'ERROR: dispatch returned {rd.status_code}: {rd.text[:200]}')
    sys.exit(1)

data = rd.json()
run_id = data.get('workflow_run_id', '')
if not run_id:
    print(f'ERROR: no run_id in response: {json.dumps(data)}')
    sys.exit(1)

print(run_id)
