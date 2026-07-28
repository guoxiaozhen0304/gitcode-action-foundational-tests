# COMP-BOUND-01-087
- **标题**: 步骤输出与跨 job 传递边界验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
ATOMGIT_OUTPUT 写入的键值对可在同 job 后续 step 中通过 steps.id.outputs 引用；跨 job 引用时仅 job outputs 中声明的键可传递。

## 做了什么
1. verify job：
   - step `Write output`(id=writer)：`echo "key1=val1" >> "$ATOMGIT_OUTPUT"` 和 `echo "key2=val2" >> "$ATOMGIT_OUTPUT"`
   - step `Read output`：`echo "K1=${{ steps.writer.outputs.key1 }}"` 和 `echo "K2=${{ steps.writer.outputs.key2 }}"` 和 `echo "output_ok"`
   - outputs 仅声明 key1
2. crossjob job (needs: verify)：`echo "DECLARED=${{ needs.verify.outputs.key1 }}"` 和 `echo "UNDECLARED=[${{ needs.verify.outputs.key2 }}]"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: K1=val1 | COVERED | echo 输出 steps.writer.outputs.key1 |
| 2 | run_logs | positive | must_contain: K2=val2 | COVERED | echo 输出 steps.writer.outputs.key2（同 job 内可访问） |
| 3 | run_logs | positive | must_contain: output_ok | COVERED | echo 固定标记 |
| 4 | run_logs | positive | must_contain: DECLARED=val1 | COVERED | needs.verify.outputs.key1 已声明，可跨 job 传递 |
| 5 | run_logs | positive | must_contain: UNDECLARED=[] | COVERED | needs.verify.outputs.key2 未声明，值为空 |
| 6 | run_logs | negative | must_not_contain: UNDECLARED=[val2] | COVERED | 未被声明传递，不应出现 val2 |
