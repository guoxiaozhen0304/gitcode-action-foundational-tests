# REL-ARTCONC-01-063
- **标题**: 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**多 job 同时 upload-artifact 同名 artifact 的并发写一致性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-063
通过标准：
1. 下载内容确定，绝非混合态
2. 内容完整无损

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate content | `python3 -c "print('A'*1048576)" > out.txt` (分支基于 `${{ matrix.instance }}`) | - | 各 matrix 实例生成 A/B/C 三种全同字符的 1MB 文件 |
| 2 | upload artifact step | `uses: upload-artifact` name=concurrent-artifact | - | 上传到同一 artifact 名 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_content in ['AAA','BBB','CCC'] | positive | - | ✅ GENUINE | 步骤真实执行 python3 生成差异化内容 + uses upload-artifact action |
| 2 | download_content contains_mixed=false | negative | - | ✅ GENUINE | 同一 artifact 名的并发上传行为由平台控制，验证点匹配 |
---
