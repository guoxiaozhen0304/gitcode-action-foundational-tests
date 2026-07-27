# COMP-DIR-01-001

- **标题**: .gitcode/workflows/ 下的 YAML 被正确识别并触发
- **维度**: completeness
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**.gitcode/workflows/ 下的 YAML 被正确识别并触发**
- 触发事件: `push`
- 规格引用: INTENT-COMP-001

通过标准：
1. [正向] 运行记录存在且 file_path 为 .gitcode/workflows/ci.yml —— 断言 run_file_path=此路径
2. [正向] 运行状态成功完成 —— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo verify | `echo "workflow recognized"` | - | 字面量字符串 |

## 3. 触发与运行环境

| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 唯一步骤仅为 echo，无条件失败路径 |
| 2 | run_file_path | positive | equals: .gitcode/workflows/ci.yml | ✅ GENUINE | harness 级断言；workflow 本身被放置于 .gitcode/workflows/ 即验证平台目录识别能力 |

### 问题

**断言 1 — STATUS_GUARANTEED**: 唯一步骤 echo "workflow recognized" 永远成功，无法验证任何目录识别能力。目录识别的验证依赖于 workflow 是否能被触发执行（harness 层面），步骤本身不做验证。

