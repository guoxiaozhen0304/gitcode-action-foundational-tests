## 失败分诊 · COMPAT-PR-01-003 · PR types 配置后匹配类型不触发与 GitHub 行为差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.pull_request.types` 使用了 GitCode 合法值 `[open, reopen, update]`，但因某些原因被平台 Schema 拒绝（可能是 step 中引用了 `atomgit.event_name` 上下文不被当 stage 支持）
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 12（`on.<event>.types` 允许值 — 当前 types 值合法）+ 可能 step `run:` 含 `${{ }}` 未加引号
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
        - name: Echo trigger info
          run: |
            echo "event_name=${{ atomgit.event_name }}"
  ```
  - `run: |` block scalar 格式中 `${{ atomgit.event_name }}` 可能导致解析问题
  - 依据规则 9，`${{ }}` 在 `run:` 中需注意，block scalar `|` 下相对安全但表达式求值可能触发平台拒绝
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 9: "运行中 `${{ }}` 可能导致解析失败，推荐双引号包裹"
  - 规则 4: 状态函数门控暂无可用的表达式中需要条件时改用 `${{ atomgit.* }}`（此处符合建议）

**置信度**: 中（types 值合法，但 `atomgit.event_name` 在 run 中的表达式可能触发平台拒绝）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回表达式错误
- **影响面**: 使用 `atomgit.event_name` 在 `run:` 中的配置
- **综合**: PR types 配置本身合法，拒绝原因可能来自表达式上下文
- **是否有规避手段**: 是 — 将 `echo "event_name=${{ atomgit.event_name }}"` 改为 `echo "event_name=manual_trigger"` 或使用 env 变量传递

**建议**:
- 将 `${{ atomgit.event_name }}` 值先注入 env 变量再引用，或直接硬编码测试值
- 排查是否为 `run: |` block scalar 中表达式的已知问题
