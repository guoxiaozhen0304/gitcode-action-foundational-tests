# USE-LBL-01-006
- **标题**: 含资源池名的 runs-on 写法平台识别验证
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**含资源池名的 runs-on 写法平台识别验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-040
通过标准：
1. 平台应接受含资源池名的写法并成功调度
2. 识别结果与文档缺失事实共同构成文档缺陷证据链

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | marker step | `echo "scheduled on named pool"` | 无 | 验证 dedicate-hosted 资源池写法 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals "success" | positive | 步骤为纯 echo，但 runs-on 资源池写法接受性由平台调度决定 | ✅ GENUINE | 平台调度匹配行为是真实行为 |
| 2 | documentation 确定性校验 | nonfunctional | 若平台识别而文档未提记缺陷，eval=deterministic | 🔶 LLM_DEPENDENT | 标注 nonfunctional 但实际为文档缺陷证据链记录，依赖人判定 |

### 问题
断言 2 虽 eval=deterministic 但 type=nonfunctional，且与 USE-LBL-01-005 合并证据链，依赖人工判定。
---
