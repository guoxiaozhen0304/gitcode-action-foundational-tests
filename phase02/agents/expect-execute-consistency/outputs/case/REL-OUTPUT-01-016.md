# REL-OUTPUT-01-016
- **标题**: step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 ATOMGIT_OUTPUT 写入恰好 1 MB 参数（1,048,576 bytes）时，下游 step 可读取完整内容。
## 做了什么
step A 通过 python3 生成 1048576 个 A 字符写入 ATOMGIT_OUTPUT 的 data 变量，step B 读取并校验长度 ≥1,048,576。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_output_length | positive | equals "1048576" | COVERED | harness 验证下游读取到的 step output 长度 |
