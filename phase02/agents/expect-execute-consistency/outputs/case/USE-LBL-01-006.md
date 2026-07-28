# USE-LBL-01-006  - **标题**: 含资源池名的 runs-on 写法平台识别验证   - **维度**: usability   - **评级**: 断言一致

## 想测什么

平台应识别该写法并按资源池调度；识别结果回写文档一致性判定

## 做了什么

- 1. 以样本中的含资源池名写法声明 runs-on 并提交 workflow
- 2. 观察平台是否识别并进入对应资源池调度

- - [正向] 平台应接受含资源池名的写法并成功调度
- - [非功能] 识别结果与文档缺失事实共同构成文档缺陷证据链（平台行为由 COMP-029 裁定）

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`success` | COVERED | run_status: runs-on:[dedicate-hosted,x64,large]格式验证→被测是平台标签解析 |
| 2 | documentation | nonfunctional | eval=deterministic | COVERED | documentation+deterministic: 平台行为与文档一致确定性判定 |
