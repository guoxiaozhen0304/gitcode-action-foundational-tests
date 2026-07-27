```
用例 ID:   COMPAT-RUNNER-01-007
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-047
参照来源:  inputs/gitcode-spec/syntax-reference/runner-images-tools.md（预装清单）; baseline/case-base-detail.md（TC-310、TC-499 FAIL）
母意图:    —（父集于 INTENT-COMPAT-NEW-011，其 Java 缺失单点证据并入本条全量对账）
标题:      Runner 预装工具链规格清单与实测全面对账

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个在 ubuntu 镜像 Runner 上逐项探测规格清单工具（java/mvn/gradle/node/go/kubectl/aws-cli）版本存在性的 workflow
  2. 触发并逐项记录实测结果，与官方预装清单逐条比对

预期结果:
  - 实际存在的工具版本与文档清单一致；文档列出但实测缺失的项记录为缺陷（当前疑似 Java 即为此类，NEW-011 单点并入）
  - setup 系列插件与预装工具的关系文档化

验证点:
  - [正向] 规格清单逐项实测：java/mvn/gradle/node/go/kubectl/aws-cli 版本存在性
  - [负向] 不应出现文档列出但实测缺失的工具而无记录
  - [非功能] 对账结果回写文档或登记文档缺陷

清理:      重置 fixture 仓库
```
