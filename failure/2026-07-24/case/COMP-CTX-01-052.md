## 失败分诊 · COMP-CTX-01-052 · 上下文在条件表达式 if 中注入验证

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持 `needs.<job_id>.result` 状态函数及 job 级 `if:` 条件表达式
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4（`if:` 表达式：仅 `always()` 确认可用，`needs.verify.result` 与 `success()` 为未经确认的状态函数）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
      if: ${{ atomgit.ref != '' }}              # job 级 if
  ...
      if: ${{ needs.verify.result == 'success' }} # needs.result 状态表达式
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 4: "success / failure 门控暂无确认可用写法：文档的裸 `success`/`failed` 与 GitHub 的 `success()` 平台都拒。未实测确认前，不要写状态门控；需要条件时改用 `${{ atomgit.* }}` 显式表达式"

**置信度**: 高（`needs.<>.result` 为状态函数语义，与规则 4 实测确认的 `success()` 被拒一致）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回具体 Schema 错误信息
- **影响面**: `needs` 上下文的 `result` 函数不可用，job 级 `if:` 未确认支持
- **综合**: 状态门控表达式（needs.result / job 级 if）不被平台接受
- **是否有规避手段**: 是 — 移除 job 级 `if:` 及 `needs.verify.result` 表达式，改用 `atomgit.*` 上下文条件或拆分断言逻辑

**建议**:
- 移除 job 级 `if:` 及 `needs.verify.result` 依赖
- 将条件逻辑改为在 step 内用 shell 判断 `if [ "$ACTION" = "expected" ]` 输出不同标记，断言扫描日志标记
