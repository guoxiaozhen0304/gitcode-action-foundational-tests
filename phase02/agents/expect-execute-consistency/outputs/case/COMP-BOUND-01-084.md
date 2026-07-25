# COMP-BOUND-01-084

- 标题: 路径与分支过滤组合及否定模式边界验证
- 维度: completeness | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

- 前置条件: 仓库已启用 AtomGit Action
- 操作步骤:
  1. 配置 push 的 branches 和 paths 组合过滤，使用否定模式
  2. 验证仅肯定模式触发，否定模式需与肯定模式组合
- 预期结果: branches 和 paths 同时存在时为 AND 关系，否定模式 ! 需与肯定模式组合，仅否定模式不触发
- 验证点:
  - [正向] branches + paths 组合过滤生效
  - [负向] 仅否定模式时不触发 workflow
  - [正向] 否定模式与肯定模式组合生效

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ok | `echo "filter_boundary_ok"` | 否 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo | default fixture |
| Secrets | 无 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] branches + paths 组合过滤生效 | ✅ | push 到匹配分支+路径触发 workflow，断言 run_status=success 且日志含 marker |
| [负向] 仅否定模式时不触发 workflow | ❌ | [负向] 本质上无法通过单次 dispatch 证明"不发生"；且实现中未定义仅含否定模式的 workflow 以尝试覆盖 |
| [正向] 否定模式与肯定模式组合生效 | ❌ | 正向匹配已验证（workflow 触发成功），但否定排除（!feature/experimental, !src/docs/**）未被专门验证；单次 dispatch 只能验证组合过滤通过，无法验证排除分支/路径确实被过滤 |

### 问题

- 唯一步骤 `echo "filter_boundary_ok"` 为纯字面量输出，无任何条件判断、表达式求值或实质逻辑，属于 trivial 步骤
- 规格要求验证"仅否定模式时不触发"，实现中完全未定义对应的 workflow（需额外定义一个 branches 仅为 `!xxx` 的 workflow，并断言不触发），且该点为 [负向] 性质，单次 dispatch 本不可证伪
- 规格要求验证否定模式与肯定模式"组合生效"——需覆盖排除侧（如推送到 `feature/experimental` 或修改 `src/docs/` 时应不触发），当前仅验证了通过侧

---
