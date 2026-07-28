## 失败分诊 · REL-POST-01-001 · post 后处理阶段失败语义

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 20 — `services` / `post.steps` 不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  jobs:
    main_ok:
      name: main success job
      runs-on: [ubuntu-latest, x64, small]
      steps: [...]
  post:
    run_always: true
    steps:
      - name: post notify step
        run: |
          echo "post_executed_marker"
          exit 1

  # 应改为（删除整个 post 块）:
  jobs:
    main_ok:
      name: main success job
      runs-on: [ubuntu-latest, x64, small]
      steps: [...]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 20: "GitCode 平台不支持 GitHub Actions 的 `jobs[id].services` 和 `post.steps`，均报 `unknown property`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有依赖后处理阶段（post steps）的 workflow
- **综合**: `post` 块是 GitHub Actions 特有语法，GitCode 平台不支持
- **是否有规避手段**: 是 — 用 `if: ${{ always() }}` 的兜底 step 替代 post 后处理逻辑

**建议**:
- 删除 `post:` 块，改为在 job 最后添加 `if: ${{ always() }}` 的清理 step
