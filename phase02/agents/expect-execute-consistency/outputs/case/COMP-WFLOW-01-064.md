# COMP-WFLOW-01-064
- **标题**: workflow stages 阶段结构字段验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**stages 为 map 格式，每个 stage 含 jobs，stage 间串行执行，fail_fast 控制失败时是否中断**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-061
通过标准：
1. stages map 格式通过校验
2. 单 stage 可缺省 stages 字段
3. fail_fast true 时某 job 失败中断后续 stage
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Build step | `echo "build_done"` | — | build_done |
| 2 | Test step | `echo "test_done"` | — | test_done |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain build_done | positive | — | ❌ VACUOUS | 步骤仅 echo，无条件分支或平台行为验证 |
| 2 | must_contain test_done | positive | — | ❌ VACUOUS | 步骤仅 echo，不验证 stage 间串行或 fail_fast 机制 |
### 问题
fail_fast 机制完全未被测试（两个 stage 均无条件成功），串行顺序也无法从 echo 日志中验证。
---
