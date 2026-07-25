# Assertion Engine（assertion-engine）

## 类型
确定性脚本（Bash + jq / Python）

## 职责
**Phase 02 最核心的确定性组件。** 对 workflow-runner 采集的 RunResult 执行断言判定，产出内部判定结论。**pass/fail 的最终裁决只由本引擎做出，LLM 绝不参与。**

> ★ 内部判定枚举（`PASS`/`FAIL`/`NOT_CONFIGURED`/`NO_RUN`/`ENV_ERROR`/`TIMEOUT`/`FLAKY`/`INCONCLUSIVE`）与其对外三态映射，**以 `phase02/rules.md` §11 判定模型为唯一权威定义**。本文中的判定示例须与 §11 保持一致；如有出入以 §11 为准。特别地：`NOT_CONFIGURED`（前置资源缺失）与 `INCONCLUSIVE`（断言语义不成立/仅间接证据）**不得判为 FAIL**。

## 依赖
- workflow-runner 产出的 `RunResult JSON`
- 用例 YAML（取 `assertions` 字段）
- `jq` / Python（JSON 解析 + 日志全文扫描）

## 输入
- `RunResult JSON`：`{ run_id, status, conclusion, duration, jobs: [...], logs: "...", artifacts: [...], fault_injection_result }`
- 用例 YAML 的 `assertions` 字段
- 用例 YAML 的 `dimension` / `priority`（辅助判断）

## 处理逻辑

### 前置检查
```python
# 0. 先检查执行层面是否正常
if run_result.status == "TIMEOUT":
    return {"verdict": "TIMEOUT", "reason": "workflow 执行超时"}
if run_result.status == "ENV_ERROR":
    return {"verdict": "ENV_ERROR", "reason": "环境错误，无法完成执行"}
```

### 逐条断言判定

```python
results = []
for assertion in case_yaml["assertions"]:
    atype = assertion["type"]
    target = assertion["target"]
    
    if atype == "positive":
        result = eval_positive(assertion, run_result)
    elif atype == "negative":
        result = eval_negative(assertion, run_result)
    elif atype == "nonfunctional":
        result = eval_nonfunctional(assertion, run_result)
    
    results.append(result)
```

### positive 断言

```python
def eval_positive(assertion, run_result):
    target = assertion["target"]
    
    if target == "run_status":
        expected = assertion.get("equals", "success")
        actual = run_result["conclusion"]  # or status
        return {
            "type": "positive",
            "target": target,
            "pass": actual == expected,
            "expected": expected,
            "actual": actual
        }
    
    elif target == "artifact":
        # 验证 artifact 存在/大小/内容
        expected_name = assertion.get("artifact_name")
        artifacts = run_result["artifacts"]
        found = any(a["name"] == expected_name for a in artifacts)
        return {
            "type": "positive",
            "target": target,
            "pass": found,
            "expected": f"artifact '{expected_name}' exists",
            "actual": "found" if found else "not found"
        }
    
    elif target == "exit_code":
        expected = assertion.get("equals", 0)
        # 从 job 详情中取 exit_code
        actual = run_result["jobs"][0].get("exit_code")
        return {
            "type": "positive",
            "target": target,
            "pass": actual == expected,
            "expected": expected,
            "actual": actual
        }
    
    # ...其他 positive target
```

### negative 断言（安全命脉）

```python
def eval_negative(assertion, run_result):
    target = assertion["target"]
    
    if target == "run_logs":
        # 全文扫描日志，确认 secret 未出现
        if "must_not_contain_secret" in assertion:
            secret_placeholder = assertion["must_not_contain_secret"]
            # ★ 注意：这里只检查占位符（如 DEPLOY_TOKEN），不检查真实值
            # 真实值永远不出现在用例/断言中
            all_logs = ""
            for job in run_result["jobs"]:
                all_logs += job.get("log", "")
            
            # 检查日志中是否出现 secret 值被打印的迹象
            # 具体检测方式：检查日志中是否有未遮蔽的敏感信息
            # （实际实现时需配合 secret 注入机制）
            leaked = detect_secret_leak(all_logs, secret_placeholder)
            
            return {
                "type": "negative",
                "target": target,
                "pass": not leaked,
                "expected": f"日志不包含 {secret_placeholder}",
                "actual": "found" if leaked else "not found",
                "is_security_critical": True
            }
    
    elif target == "secret_access":
        # 验证 fork 身份无 secret 访问权限
        # 检查 run 的 permissions 上下文
        return {
            "type": "negative",
            "target": target,
            "pass": run_result.get("secret_access") == "denied",
            "expected": "secret access denied",
            "actual": run_result.get("secret_access", "unknown")
        }
    
    elif target == "side_effect":
        # 验证无越权副作用（如未授权 push、未授权 PR 评论等）
        pass
```

### nonfunctional 断言

```python
def eval_nonfunctional(assertion, run_result):
    target = assertion["target"]
    
    if target == "latency":
        threshold = assertion.get("max_duration_seconds", 600)
        actual = run_result["duration"]
        return {
            "type": "nonfunctional",
            "target": target,
            "pass": actual <= threshold,
            "expected": f"duration <= {threshold}s",
            "actual": f"{actual}s"
        }
    
    elif target == "concurrency_isolation":
        # 验证并发执行互不干扰
        pass
    
    elif target == "error_message":
        # 验证错误信息包含可定位上下文
        if assertion.get("eval") == "llm_assisted":
            # 易用性主观判据 → 交给 LLM 辅助评分
            # 但这里仍产出一个确定性基线（如关键词匹配）
            rubric = assertion.get("rubric", "")
            logs = run_result["logs"]
            # 确定性部分：至少包含行号
            has_line_number = check_error_has_line_number(logs)
            return {
                "type": "nonfunctional",
                "target": target,
                "pass": has_line_number,  # 确定性基线
                "llm_assisted": True,
                "rubric": rubric,
                "expected": "错误信息包含行号",
                "actual": "contains line number" if has_line_number else "no line number"
            }
```

### 汇总判定

```python
def overall_verdict(assertion_results):
    # 所有断言都 pass → PASS
    if all(r["pass"] for r in assertion_results):
        return "PASS"
    
    # 有 failure 且是安全关键断言 → FAIL (with security flag)
    security_fails = [r for r in assertion_results if not r["pass"] and r.get("is_security_critical")]
    if security_fails:
        return "FAIL", "SECURITY_CRITICAL"
    
    # 有 failure 但非安全关键 → FAIL
    return "FAIL"
```

## 输出
```json
{
  "case_id": "SEC-FORK-01-001",
  "verdict": "FAIL",
  "verdict_flags": ["SECURITY_CRITICAL"],
  "assertion_results": [
    {
      "type": "negative",
      "target": "run_logs",
      "pass": false,
      "expected": "日志不包含 DEPLOY_TOKEN",
      "actual": "found at job log line 42",
      "is_security_critical": true
    },
    {
      "type": "positive",
      "target": "run_status",
      "pass": true,
      "expected": "success",
      "actual": "success"
    }
  ],
  "duration": "2m34s",
  "log_fingerprint": "abc123..."  # 日志哈希，用于去重/flaky 检测
}
```

## 质量要求
- **确定性**：同一份 RunResult + assertions 多次判定结果必须一致
- **可复核**：每条断言的 expected/actual 必须可让人看懂
- **安全断言零容忍**：negative 断言失败自动标记 `SECURITY_CRITICAL`
- **LLM 辅助断言**显式标注 `llm_assisted: true`，且必须有确定性基线作为 fallback

## 已实现 kind 清单（2026-07-25 扩展，以 assertion_engine.py docstring 为准）

| kind | 参数 | 语义 | 数据依赖 |
|------|------|------|----------|
| `status` | — | 所有 job/step 全绿（含假绿守卫） | jobs |
| `run_status` / `run_status_not` | `equals` / `not_equals` | run 级终态比对（词形归一） | conclusion |
| `job_status` | `equals`, `name?` | job 级终态；`name` 为 job name/id 子串 hint，无匹配 → INCONCLUSIVE | jobs[].status |
| `step_status` | `equals`, `name?` | step 级终态，规则同上 | jobs[].steps[] |
| `job_count` | `equals: N` | job 实例总数（matrix 展开计数） | jobs |
| `job_count_by_status` | `status`, `equals: N` | 指定终态的 job 数（如 CANCELLED） | jobs |
| `value` | `expect` | 日志包含指定串 | logs |
| `value_in` | `any_of: [...]` | 日志至少包含其一 | logs |
| `leak` / `mask` | `forbidden` / `secret_value` | 安全负向断言（SECURITY_CRITICAL） | logs |
| `log_metric_le` | `metric`, `le` | 日志 `metric=N` 且 N ≤ le；无标记 → INCONCLUSIVE | logs |
| `log_metric_delta_le` | `start`, `end`, `le` | 日志时间戳对差值 ≤ le（workflow 内自打 `date +%s`） | logs |
| `duration_le` | `le` | run duration ≤ le 确凿 pass；超出 → INCONCLUSIVE（上界近似，不反推 FAIL） | duration_seconds |
| `config_probe` | `unconfigured_pattern?` | 前置资源探测，未配置 → NOT_CONFIGURED | logs |

编译侧（compile_asserts.py）对应映射：
- `job_status`/`job_x_status` → `job_status`（带 name hint）；`step_status`/`step_conclusion` → `step_status`；
  `workflow_status` 并入 run 级 `run_status`。
- `generated_jobs_count` → `job_count`；`cancelled_jobs_count` → `job_count_by_status(CANCELLED)`。
- `<x>_time_seconds + le` → `log_metric_delta_le(<x>_start, <x>_end)`；
  `scheduling_latency_seconds + le` → `duration_le`。
- `hash_match equals v` → `value("hash_match=v")`；`download_content in [...]` → `value_in`；
  `download_content contains_mixed v` → `value("contains_mixed=v")`。

### 终态复合标记（2026-07-25 第二轮）

`run_status` / `run_status_not` / `job_status` / `step_status` 的期望值支持复合标记，
由 `_terminal_match` 统一处理（大小写不敏感）：

- **`A_OR_B` 多值**：任一可选终态命中即 pass。例：`SUCCESS_OR_FAILURE`、`COMPLETED_OR_BLOCKED`、
  `failure_or_canceled`。用于"成功或被拒都算符合安全预期"的断言。
- **`X_WITH_Y` 复合**：`WITH` 后的语义无法从 conclusion 判定，按主状态 `X` 近似。
  例：`SUCCESS_WITH_BASE_WORKFLOW` → 按 SUCCESS 判定；with 语义由配套 leak/value 断言覆盖。

编译器 `_NO_DATASOURCE_TARGETS` 同步补充 `step_summary_html`。
