# SEC-NET-01-001

- 标题: Runner 网络出站必须受控，防止 SSRF 与内网跳板
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了自托管或官方 runner
操作步骤:
  1. 1. 提交一个 workflow，尝试访问内部元数据端点或内网地址
  2. 2. 触发 workflow 并查看网络访问结果
预期结果:
  - 访问尝试返回超时或连接拒绝
  - 运行日志中无外发成功记录

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Access metadata endpoint | curl -s --max-time 5 http://169.254.169.254/ \|\| echo "access denied or timeout"  | 是 |
| 2 | Access internal IP | curl -s --max-time 5 http://192.168.1.1/ \|\| echo "access denied or timeout"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: metadata_service_response | UNCOVERED | 期望值 [metadata_service_response] 未在任何步骤输出中找到 |
| [positive] run_logs equals: access_denied_or_timeout | UNCOVERED | 期望值 [access_denied_or_timeout] 未在任何步骤输出中找到 |

### 问题

- **断言 1 - MISSING_SOURCE**: 期望值 [metadata_service_response] 未在任何步骤输出中找到
- **断言 2 - MISSING_SOURCE**: 期望值 [access_denied_or_timeout] 未在任何步骤输出中找到

---
