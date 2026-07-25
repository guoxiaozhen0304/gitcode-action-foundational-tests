# COMPAT-CONTAINER-01-002

- 标题: container 自定义镜像被拒绝时应给出替代指引
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-CONTAINER-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-NEW-001
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      container 自定义镜像被拒绝时应给出替代指引

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个包含 `jobs.<id>.container.image` 为自定义镜像的 workflow 文件
  2. 该镜像为内部 Registry 地址（如 `myregistry.com/build-env:v1`）
  3. 提交该 workflow 到仓库

预期结果:
  - 系统拒绝该 workflow 或拒绝拉取该镜像
  - 报错信息应说明 container 自定义镜像不被支持
  - 若 container 字段整体不支持，报错应提示使用默认 Runner 环境替代

验证点:
  - [正向] 报错信息说明 container 自定义镜像限制
  - [正向] 报错给出替代方案（如使用默认 Runner 或指定 runs-on 标签）

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo hello (test-custom-image) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 报错信息说明 container 自定义镜像限制 | 覆盖 | LLM/nonfunctional assertion: 报错给出替代方案，如使用默认 Runner 环境或指定 runs-on 标签 |
| 报错给出替代方案（如使用默认 Runner 或指定 runs-on 标签） | 覆盖 | LLM/nonfunctional assertion: 报错给出替代方案，如使用默认 Runner 环境或指定 runs-on 标签 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error | negative | 报错信息说明 container 自定义镜像不被支持 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息说明 container 自定义镜像不被支持 |
| 2 | error_message | positive | 报错给出替代方案，如使用默认 Runner 环境或指定 runs-on 标签 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错给出替代方案，如使用默认 Runner 环境或指定 runs-on 标签 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
