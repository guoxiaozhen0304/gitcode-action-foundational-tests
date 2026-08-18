
Issue 除了基本的创建、编辑和评论功能外，GitCode 还提供了一系列其他操作，以增强项目管理和协作。下面我们将为你介绍 GitCode Issue 中可进行的操作，以帮助你更好地利用这些功能来管理项目。

## 可进行的操作

### 标签（Labels）

Label 是用于对 Issue 进行分类、筛选和组织的关键工具。通过为 Issue 添加标签，你可以更容易地识别和处理不同类型的问题，例如 bug、功能请求、优化等。在每个项目初始化的时候，系统会为项目创建一组通用的 Label（详见下表）

| Label 名称 | 描述 | 
|--|--|
| `wontfix` | This will not be worked on |
| `question` | Further information is requested |
| `invalid` | This doesn't seem right |
| `help wanted` | Extra attention is needed |
| `enhancement` | New feature or request |
| `duplicate` | This issue or merge request or discussion already exists |
| `documentation` | Improvements or additions to documentation |
| `bug` | Something isn't working |

### 里程碑（Milestones）

里程碑允许你将 Issue 分组到特定的版本或项目阶段中。这有助于项目管理者和开发者跟踪和计划工作的进度，并为每个里程碑分配截止日期。

### 分配（Assignees）

分配 Issue 给特定的团队成员或个人，以明确责任和分工。被分配的人将负责解决问题或任务，并可以跟踪 Issue 的状态。

### 关联 Issue（Linked Issues）

你可以在 Issue 之间创建关联，以显示它们之间的关系。这对于解决问题之间的依赖关系或相关性非常有用。

### 锁定和解锁（Locking and Unlocking）

对于可能引发争议或不当行为的 Issue，你可以选择锁定它们，以防止进一步的评论和更改。解锁 Issue 后，其他用户可以再次进行评论和更改。

### 置顶和取消置顶（Pin and Unpin）

对于重要的 issue，你可以选择置顶它们，使其始终位于项目 Issue 列表的顶部。取消置顶后，允许 Issue 根据最新活动重新排序。

### 关闭和重新打开（Closing and Reopening）

当 Issue 已解决或任务已完成时，你可以将 Issue 标记为关闭。如果需要重新打开 Issue 以重新讨论或修复，你也可以重新打开它。

### 自动关闭（Auto-closing）

通过提交带有特定关键字的提交消息，你可以自动关闭相关的 Issue 。例如，当提交包含"Fixes #123"时，GitCode 将自动关闭 Issue ID 为 123 的 Issue。

## 最佳实践

以下是一些 Issue 的最佳实践：

- 使用标签和里程碑来组织和计划工作
- 分配 Issue 以明确责任
- 创建关联 Issue 以建立 Issue 之间的关系
- 适时锁定 Issue 以防止不必要的评论
- 及时关闭已解决的 Issue ，以保持 Issue 列表的清晰度

通过了解 GitCode Issue 中可进行的操作，你可以更好地管理项目，提高团队协作和 Issue 解决的效率。