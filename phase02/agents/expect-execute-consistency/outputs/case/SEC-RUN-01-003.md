# SEC-RUN-01-003

- 标题: 自托管 Runner 跨项目残留必须被隔离
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 自托管 runner 被多个项目共享
操作步骤:
  1. 1. 项目 A 的 workflow 写入临时文件和环境变量
  2. 2. 项目 B 的 workflow 在同一 runner 上检查残留
预期结果:
  - 项目 B 的 job 绝不应读取到项目 A 残留的敏感文件或环境变量
  - runner 清理失败时应标记为不可用

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write temp | echo project-a-secret > /tmp/project-a-temp.txt  | 是 |
| 2 | Check no cross project leak | if [ -f /tmp/project-a-temp.txt ]; then   echo "cross project leak"   exit 1 else   echo "isolated as expected" fi  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: cross project leak | COVERED | 步骤 [Check no cross project leak] 执行真实功能时输出该值 |
| [positive] run_logs equals: isolated_as_expected | UNCOVERED | 期望值 [isolated_as_expected] 未在任何步骤输出中找到 |

### 问题

- **断言 2 - MISSING_SOURCE**: 期望值 [isolated_as_expected] 未在任何步骤输出中找到

---
