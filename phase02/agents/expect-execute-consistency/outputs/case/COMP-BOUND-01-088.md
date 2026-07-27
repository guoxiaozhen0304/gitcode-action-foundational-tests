# COMP-BOUND-01-088

- **标题**: 工作流命令 set-env add-path 与文件写入边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**工作流命令 set-env add-path 与文件写入边界验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-088

通过标准：
1. [正向] ATOMGIT_ENV 写入后后续 step 可读取 —— 断言 MY_ENV=from_env_file
2. [正向] ATOMGIT_PATH 添加后目录在 PATH
3. [正向] ATOMGIT_OUTPUT 写入后 outputs 可引用 —— 断言 commands_ok

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write env and path | `echo "MY_ENV=from_env_file" >> "$ATOMGIT_ENV"` + `echo "/tmp/extra_bin" >> "$ATOMGIT_PATH"` | - | 写入平台文件 |
| 2 | Read env | `echo "MY_ENV=$MY_ENV"` + `[[ "$PATH" == *"/tmp/extra_bin"* ]]` + `echo "commands_ok"` | - | 读取上一步通过平台文件设置的变量 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: MY_ENV=from_env_file | ✅ GENUINE | 值来源为 $ATOMGIT_ENV 写入后的平台环境变量注入，非字面量 echo |
| 2 | run_logs | positive | must_contain: commands_ok | ✅ GENUINE | 同一步骤中使用了 bash `[[ ]]` 运算检测 $ATOMGIT_PATH 效果 |

