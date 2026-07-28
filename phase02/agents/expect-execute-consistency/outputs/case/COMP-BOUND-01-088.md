# COMP-BOUND-01-088
- **标题**: 工作流命令 set-env add-path 与文件写入边界验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
ATOMGIT_ENV 写入的环境变量在当前 job 后续 step 中可用，ATOMGIT_PATH 添加的目录在 PATH 中，ATOMGIT_OUTPUT 写入的键值可被引用。

## 做了什么
1. step `Write env path and output`(id=cmdwriter)：
   - `echo "MY_ENV=from_env_file" >> "$ATOMGIT_ENV"`
   - `echo "/tmp/extra_bin" >> "$ATOMGIT_PATH"`
   - `echo "out_key=out_val" >> "$ATOMGIT_OUTPUT"`
2. step `Read env`：`echo "MY_ENV=$MY_ENV"`、检查 PATH 是否含 /tmp/extra_bin、`echo "OUT_KEY=${{ steps.cmdwriter.outputs.out_key }}"` 和 `echo "commands_ok"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: MY_ENV=from_env_file | COVERED | echo $MY_ENV 输出 ATOMGIT_ENV 写入的值 |
| 2 | run_logs | positive | must_contain: PATH_HAS_EXTRA=yes | COVERED | bash `[[ "$PATH" == *"/tmp/extra_bin"* ]]` 检查 ATOMGIT_PATH 效果 |
| 3 | run_logs | positive | must_contain: OUT_KEY=out_val | COVERED | steps.cmdwriter.outputs.out_key 引用 ATOMGIT_OUTPUT 写入的值 |
| 4 | run_logs | positive | must_contain: commands_ok | COVERED | echo 固定标记 |
