# REL-MEM-01-020
- **标题**: Runner 内存边界——small runner 分配 7.5 GB 应成功
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Runner 内存边界——small runner 分配 7.5 GB 应成功**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-020
通过标准：
1. job 状态 = success

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | allocate 7.5GB | `python3 -c "a=bytearray(7680*1024*1024); print(len(a))"` | — | 分配 7.5GB 内存并输出字节数 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = success | positive | — | ✅ GENUINE | `python3 -c` 真实分配 7680*1024*1024 字节内存，确实测试 small runner 的 7.5GB 内存边界 |
---
