# SEC-LOG-01-002

- **标题**: 导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-040

通过标准：
1. type=positive, target=log_api, equals=download_ok
2. type=negative, target=exported_logs, must_not_contain_secret="DEPLOY_TOKEN"
3. type=negative, target=historical_logs, must_not_contain_secret="DEPLOY_TOKEN"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Reference secret in log | `echo "MASKED_SECRET_LINE: ${{ secrets.DEPLOY_TOKEN }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  masked-log-producer:
    name: Produce masked secret log
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Reference secret in log
        run: |
          echo "MASKED_SECRET_LINE: ${{ secrets.DEPLOY_TOKEN }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_api | positive | equals=download_ok | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | exported_logs | negative | !secret=DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 DEPLOY_TOKEN，secret 脱敏断言有验证对象（故意暴露测试） |
| 3 | historical_logs | negative | !secret=DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 DEPLOY_TOKEN，secret 脱敏断言有验证对象（故意暴露测试） |

---