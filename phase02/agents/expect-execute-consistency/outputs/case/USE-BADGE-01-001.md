# USE-BADGE-01-001

- 标题: workflow 运行完成后状态徽标及时回写且语义清晰
- 维度: usability | 优先级: P1
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - PR 存在且关联了 workflow
操作步骤:
  1. 1. 触发 workflow 运行
  2. 2. 完成后检查 Commits 页面与 PR Checks 标签页
预期结果:
  状态徽标在 30 秒内刷新，成功/失败/跳过图标语义清晰、颜色可辨

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | success step | echo "success"  | 否 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [positive] run_status equals: COMPLETED | UNCOVERED | 所有步骤无实质逻辑/条件/action，workflow 永远成功 |
| [nonfunctional] ui_visual  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 状态徽标在 Commits 列表中尺寸 >= 16x16px，颜色含义符合行业惯例（绿=成功、红=失败、黄=运行中、灰=跳过/取消）；鼠标悬停徽标时显示 too |

### 问题

- **断言 1 - STATUS_GUARANTEED**: 所有步骤无实质逻辑/条件/action，workflow 永远成功
- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 状态徽标在 Commits 列表中尺寸 >= 16x16px，颜色含义符合行业惯例（绿=成功、红=失败、黄=运行中、灰=跳过/取消）；鼠标悬停徽标时显示 too
- **整体空洞**: 所有步骤均无实质逻辑（仅 echo/无 action/无 if 条件）

---
