# COMP-ARTIFACT-01-003

- **标题**: artifact 保留期设置生效
- **维度**: completeness
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**artifact 保留期设置生效**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-015

通过标准：
1. [正向] 保留期内可下载 artifact —— 断言 artifact_available=yes_within_retention
2. [负向] 超过保留期后下载返回 404 —— 断言 artifact_available_after_expiry=no_after_1_day

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Create artifact | `echo "temp" > temp.txt` | - | 生成文件 |
| 2 | Upload artifact | `uses: upload-artifact` with retention-days: 1 | - | 上传制品并设置保留期 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_available | positive | equals: yes_within_retention | ✅ GENUINE | workflow 真实上传了带 retention-days: 1 的制品，harness 级断言验证保留期内可访问 |
| 2 | artifact_available_after_expiry | negative | equals: no_after_1_day | ✅ GENUINE | harness 级断言验证超期后不可访问，workflow 已正确设置场景 |

