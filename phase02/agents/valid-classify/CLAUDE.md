# Valid-Classify / 平台校验分类

## 角色定位

将 scriptable 用例提交到 GitCode 平台校验 API，按返回值分组：通过校验 → `valid/`，拒绝 → `invalid/`，WAF 拦截 → 白名单通过。

不在本步关注 workflow 语义、断言一致性或可脚本化性——这些已在 expect-execute-consistency 和 scriptable-classify 中完成。

## 输入

| 来源 | 路径 |
|------|------|
| 可脚本化用例 | `phase02/agents/scriptable-classify/output/scriptable/*.yaml` |

## 判定规则

| API 响应 | 分组 |
|----------|------|
| HTTP 200 + code=0 | `valid/` |
| HTTP 200 + code≠0 或 HTTP 非 200 非 418 | `invalid/` |
| HTTP 418 (CloudWAF) | `valid/`（白名单通过，WAF 误拦截） |

**WAF 白名单**：以下 case ID 被 WAF 拦截但之前人工/流水线验证可通过，直接放入 `valid/`：

| Case ID | 拦截原因 |
|---------|------|
| COMP-ATOMGIT-01-047 | workflow body 含 `${}` 触发 WAF，人工验证通过 |
| COMP-ATOMGIT-01-048 | 同上 |
| COMP-ATOMGIT-01-049 | 同上 |
| COMP-SCRIPT-01-082 | 同上 |
| COMPAT-TOKEN-01-001 | token 值在 YAML 中触发注入检测 |
| COMPAT-TOKEN-01-002 | 同上 |
| REL-LOG-01-040 | 日志相关表达式触发 WAF |
| REL-OUTPUT-01-017 | ATOMGIT_OUTPUT 相关模式触发 WAF |
| USE-MASK-01-001 | secret masking 相关 |
| SEC-NAME-01-002 | secret 名触发 WAF |
| SEC-ENV-WAIT-02-001 | 环境等待相关 |

非白名单中的 418 响应 → `invalid/`。

## 工作步骤

### Step 1: 逐文件校验

执行 `phase02/agents/valid-classify/batch_validate.py`：

```bash
python3 phase02/agents/valid-classify/batch_validate.py \
  phase02/agents/scriptable-classify/output/scriptable/ \
  phase02/agents/valid-classify/output/
```

脚本内置 WAF 白名单，自动将白名单中的 418 响应归入 `valid/`。

### Step 2: 按响应分组

| 响应 | 操作 |
|------|------|
| 200 + code=0 | YAML 复制到 `valid-classify/output/valid/` |
| 200 + code≠0 | YAML 复制到 `valid-classify/output/invalid/`，记录诊断信息 |
| 418 + 在白名单 | YAML 复制到 `valid-classify/output/valid/`，记录 `WAF_WHITELIST` |
| 418 + 不在白名单 | YAML 复制到 `valid-classify/output/WAF/` |
| 其他错误 | YAML 复制到 `valid-classify/output/invalid/` |

### Step 3: 输出

```
valid-classify/output/
├── valid/          ← 平台校验通过（含 WAF 白名单）
├── invalid/        ← 平台拒绝
├── WAF/            ← WAF 拦截（非白名单）
└── report.md
```

输出到 `phase02/agents/valid-classify/output/report.md`：

```markdown
# Valid Classify Report

## 总览

| 分组 | 数量 |
|------|:---:|
| valid | N (+N WAF whitelist) |
| invalid | N |
| WAF | N |
| SKIP | N |

## WAF 白名单

| Case ID | 拦截原因 |
|---------|------|
| COMP-ATOMGIT-01-047 | workflow body 含 `${}` 触发 WAF，人工验证通过 |
| COMP-ATOMGIT-01-048 | 同上 |
| COMP-ATOMGIT-01-049 | 同上 |
| COMP-SCRIPT-01-082 | 同上 |
| COMPAT-TOKEN-01-001 | token 值在 YAML 中触发注入检测 |
| COMPAT-TOKEN-01-002 | 同上 |
| REL-LOG-01-040 | 日志相关表达式触发 WAF |
| REL-OUTPUT-01-017 | ATOMGIT_OUTPUT 相关模式触发 WAF |
| USE-MASK-01-001 | secret masking 相关 |
| SEC-NAME-01-002 | secret 名触发 WAF |
| SEC-ENV-WAIT-02-001 | 环境等待相关 |

## invalid 明细

| Case ID | 诊断 |
|---------|------|
| xxx | error_msg... |
```

## 护栏

- 请求间隔 ≥ 0.8 秒。
- WAF 白名单为硬编码，不同批次运行时确认是否仍然有效。
- 不修改源 YAML，仅复制分组。