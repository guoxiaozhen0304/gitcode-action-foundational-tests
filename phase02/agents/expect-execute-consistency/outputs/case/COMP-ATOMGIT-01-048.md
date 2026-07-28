# COMP-ATOMGIT-01-048
- **标题**: atomgit 事件相关属性可访问性
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
push 事件下 atomgit.event 下各字段（ref/before/after/commits/base_ref/created/deleted）可正常访问。

## 做了什么
1. step `Print event properties`：echo 各 atomgit.event 属性
2. step `Check event ref consistency`：对比 `${{ atomgit.event.ref }}` 与 `${{ atomgit.ref }}` 是否一致并输出
3. step `Check sha formats and commits`：正则校验 before/after 为 40 位 hex，输出 commits 长度

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: EVENT_REF=refs/ | COVERED | `echo "EVENT_REF=${{ atomgit.event.ref }}"` 输出 |
| 2 | run_logs | positive | must_contain: BEFORE_HEX40=yes | COVERED | bash `[[ "$BEFORE" =~ ^[0-9a-f]{40}$ ]]` 校验后 echo |
| 3 | run_logs | positive | must_contain: AFTER_HEX40=yes | COVERED | bash 正则校验后 echo 输出 |
| 4 | run_logs | positive | must_contain: COMMITS_LEN= | COVERED | `${#COMMITS}` 输出长度 |
| 5 | run_logs | positive | must_contain: REF_CONSISTENT=yes | COVERED | if 比较后 echo 输出 |
