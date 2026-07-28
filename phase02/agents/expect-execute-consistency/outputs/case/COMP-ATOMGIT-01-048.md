# COMP-ATOMGIT-01-048

- **标题**: atomgit 事件相关属性可访问性
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 push 事件下 `atomgit.event.ref`、`before`、`after`、`commits`、`base_ref`、`created`、`deleted` 等字段可正常访问，before/after 为 40 位 SHA，event.ref 与 atomgit.ref 一致。

## 做了什么
三个 step：打印事件属性、用 bash `if [...]` 校验 event.ref 与 atomgit.ref 一致性、用 bash 正则 `[[ =~ ^[0-9a-f]{40}$ ]]` 校验 before/after 格式 + 输出 commits 长度。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: EVENT_REF=refs/ | COVERED | `echo "EVENT_REF=${{ atomgit.event.ref }}"` 直接产生 |
| 2 | run_logs | positive | must_contain: BEFORE_HEX40=yes | COVERED | bash `[[ $BEFORE =~ ^[0-9a-f]{40}$ ]]` 实际校验后 echo 输出 |
| 3 | run_logs | positive | must_contain: AFTER_HEX40=yes | COVERED | 同上，对 AFTER 做 40 位 hex 正则校验 |
| 4 | run_logs | positive | must_contain: COMMITS_LEN= | COVERED | echo `${#COMMITS}` 输出长度 |
| 5 | run_logs | positive | must_contain: REF_CONSISTENT=yes | COVERED | bash `[ "${{ atomgit.event.ref }}" = "${{ atomgit.ref }}" ]` 实际比较后 echo 输出 |
