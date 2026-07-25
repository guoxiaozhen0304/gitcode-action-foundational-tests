# SEC-NAME-01-001

- 标题: Secret/变量名含特殊字符时不可导致意外求值或权限绕过
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了含中划线的 secret MY-VAR
操作步骤:
  1. 1. 提交一个 workflow，引用 secrets.MY-VAR 并在 shell 中使用
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - 含中划线的 secret 不应因解析错误而被泄露到日志
  - 若不支持中划线，应在 YAML 校验阶段报错

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Use hyphen secret | echo "value is ${{ secrets.MY-VAR }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: MY-VAR | COVERED | 步骤使用了 MY-VAR，平台需在日志中脱敏 |
| [positive] run_status equals: success_or_yaml_error | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |

### 问题

- 无

---
