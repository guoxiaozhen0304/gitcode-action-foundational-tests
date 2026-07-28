## 失败分诊 · REL-RACE-01-048 · 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4 — `if:` 表达式：`${{ }}` 包裹 + `always()` 带括号
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  job_b:
    needs: job_a
    if: failure()

  # 应改为（当前唯一确认可用的状态函数是 always()）:
  job_b:
    needs: job_a
    if: ${{ always() }}
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 4: "`if: ${{ failure() }}`（GitHub 语法）→ ❌ 拒绝：`表达式：failure() 第1位出现不支持的函数`。" `failure()` 是 GitHub 语法（带括号函数调用），GitCode 平台仅确认支持 `${{ always() }}`。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回表达式函数不支持错误
- **影响面**: 所有使用 GitHub 状态函数 `failure()` / `success()` 的工作流
- **综合**: `failure()` 是 GitHub 语法，GitCode 仅支持 `${{ always() }}`，该表达式直接报错
- **是否有规避手段**: 是 — 改用 `if: ${{ always() }}` 作为兜底条件

**建议**:
- 将 `if: failure()` 替换为 `if: ${{ always() }}`；精确的 failure 门控需等待平台确认 `${{ failed }}` 的可用性
