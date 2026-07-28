# REL-OUTPUT-01-016
- **标题**: step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
step向ATOMGIT_OUTPUT写入1MB参数，下游读取完整1048576字节，不应截断。

## 做了什么
writer step写出1MB数据，reader step读取并校验长度≥1048576。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_output_length | positive | equals=1048576 | COVERED | 文本"下游读取内容长度=1,048,576 bytes"精确对应(step内wc -c校验≥1048576) |
