# Feature Specification: Dialog UI Redesign

**Feature Branch**: `002-dialog-ui-redesign`  
**Created**: 2025-12-09  
**Status**: Draft  
**Input**: User description: "我需要在当前项目中统一重新设计 对话界面的所有 UI 元素显示效果，需要一份完整的设计文档包含所有的对话内容。让其显示效果美观、动态。"

## User Scenarios & Testing _(mandatory)_

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Readable conversational stream (Priority: P1)

用户进入对话页，快速理解整段对话流，区分人类消息、AI 回复、工具调用与子代理输出，且在滚动或新消息到达时保持视觉层次和节奏感。

**Why this priority**: 直接决定聊天核心体验与可用性。  
**Independent Test**: 仅实现消息流与基础视觉语言即可完整演示（含滚动、Markdown、子代理标识、工具调用概要）。

**Acceptance Scenarios**:

1. **Given** 对话中混合人类/AI/工具消息，**When** 用户浏览消息流，**Then** 不同类型在外观、对齐、标识上清晰区分且不遮挡内容。
2. **Given** AI 回复含代码/列表/链接/长文本，**When** 渲染完成，**Then** Markdown 样式统一且长内容不破版，可在桌面与移动宽度下正常阅读。

---

### User Story 2 - Trustworthy tool interactions (Priority: P2)

用户在对话流中查看工具调用（包括生成式 UI、审批、回退展示），能一眼看出状态，展开细节或审批操作，并在中断/继续时获得明确反馈。

**Why this priority**: 工具调用是工作结果与风险的核心触点，需高可见性和可控性。  
**Independent Test**: 仅实现工具卡片（含状态徽标、摘要、展开/收起、审批表单）即可独立测试。

**Acceptance Scenarios**:

1. **Given** 工具调用处于 pending/完成/错误/中断，**When** 用户查看卡片，**Then** 状态徽标与颜色标签一致、摘要语清晰且可点击展开细节。
2. **Given** 工具需要审批，**When** 用户选择批准/拒绝/编辑后提交，**Then** UI 显示所选决策与结果摘要，并可在不中断对话的情况下返回消息流。

---

### User Story 3 - Manage threads, tasks, and files with clarity (Priority: P3)

用户在同一界面中切换线程、查看/收起任务与文件侧栏、打开配置或文件查看弹窗，依然保持一致的主题、间距与动效，不干扰对话阅读。

**Why this priority**: 多上下文管理（线程/任务/文件/配置）是高频操作，需要统一的导航与层级感。  
**Independent Test**: 仅实现线程列表与任务/文件区域的统一样式与动效即可独立演示价值。

**Acceptance Scenarios**:

1. **Given** 用户展开/收起任务与文件区域，**When** 内容从空到有或切换 tab，**Then** 过渡平滑、计数徽标与标题对齐，且不会挡住消息流。
2. **Given** 用户打开线程列表或配置弹窗，**When** 操作完成或关闭，**Then** 返回对话区的滚动位置与输入状态保持不变。

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

- 极长对话（上百条消息）或超长代码块时，消息流仍保持可滚动、分段渲染与清晰的行高/留白。
- 工具返回缺省 UI 组件时（无 `uiComponent`），仍展示摘要、参数与结果的回退样式；生成式 UI 加载失败时提供降级提示。
- 流被中断或网络抖动时，状态条/按钮显式展示「中断」与「重试/继续」，避免用户误判；错误态与空态的视觉区分明显。
- 任务/文件数为 0 → N 或 N → 0 时，侧栏自动收起/展开策略不影响当前阅读位置。
- 线程列表加载失败或为空时，提示语与重试入口清晰，不出现空白。

## Requirements _(mandatory)_

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001 视觉系统统一**：为对话页所有主要组件建立一致的主题、字体层级、间距、圆角、阴影与色彩语义，覆盖 `ChatInterface`、`ChatMessage`、`ToolCallBox`、`ToolApprovalInterrupt`、`MarkdownContent`、`TasksFilesSidebar`、`ThreadList`、`ConfigDialog`、`FileViewDialog`（路径如 `deep-agents-ui/src/app/components/...`）。
- **FR-002 消息层级与可读性**：人类/AI/工具/子代理消息在版式上明确区分（对齐、背景、徽标、头像/标识），Markdown/代码块/列表/链接在窄宽与宽屏均保持行高和断行策略，不出现水平溢出。
- **FR-003 工具卡片状态表达**：`ToolCallBox` 展示统一的状态徽章（pending/完成/错误/中断）、摘要行与图标，点击可展开详情；支持已知工具类型的专用视图（搜索/读写/编辑文件、ls、todo），对未知类型提供参数+结果回退展示。
- **FR-004 审批交互**：`ToolApprovalInterrupt` 以卡片式呈现审批说明、参数、可选拒绝理由、可编辑参数区；操作按钮（批准/拒绝/编辑）有禁用与加载态，提交后反馈结果摘要。
- **FR-005 生成式 UI 与降级**：当存在 `uiComponent`（生成式 UI）时，确保加载区域与对话风格一致，加载/失败时显示占位与重试；无生成式 UI 时默认回退至参数+结果视图，不阻塞消息流。
- **FR-006 任务与文件区域**：`TasksFilesSidebar` / 内联任务文件区提供可折叠标题、计数徽标、分组状态（pending/in_progress/completed），新增任务或文件时可配置自动展开；`FilesPopover` + `FileViewDialog` 需有清晰的卡片、悬停、空态、禁用编辑态。
- **FR-007 线程列表一致性**：`ThreadList` 的过滤、分组、选中、加载/空/错误态使用与对话页一致的色彩与留白；中断线程的高亮与 badge 明确，不影响当前对话滚动。
- **FR-008 输入与流控制**：输入区在加载/闲置/中断时的占位、按钮文案与禁用态一致；支持 Enter 发送、Shift+Enter 换行，停止/继续操作的视觉反馈明显且不遮挡输入。
- **FR-009 弹窗与遮罩**：`ConfigDialog`、`FileViewDialog` 的遮罩、圆角、标题、按钮排布与全局主题一致；关闭后恢复先前滚动位置与焦点，不影响消息流。
- **FR-010 动效与可达性**：核心交互（展开/收起、状态切换、按钮悬停）具备轻量过渡动画（200–300ms 级别），同时保留键盘可达性与可见焦点样式，避免眩光或过度动画。

### Key Entities _(include if feature involves data)_

- **Message**：type（human/ai/tool）、content（文本/Markdown/代码）、id、tool_calls、metadata（滚动锚点、ui 绑定）。
- **ToolCall**：name、args、status（pending/completed/error/interrupted）、result、uiComponent、actionRequest/reviewConfig。
- **SubAgent**：id、subagent_type、input/output、status（继承 ToolCall）。
- **Task (TodoItem)**：id、content、status（pending/in_progress/completed）。
- **FileItem**：path、content、editability；与 FilesPopover/FileViewDialog 关联。
- **Thread**：id、title、description、status（idle/busy/interrupted/error）、updatedAt；与 ThreadList 分组过滤相关。
- **UI Block**：来自后端的 `ui` 片段，绑定 message_id/tool_call_id，用于生成式 UI 区域。

## Assumptions & Dependencies

- 现有对话流/线程/任务/文件的后端数据结构保持不变，重新设计聚焦前端呈现与交互。
- 主题色、字体、间距与图标基于当前设计令牌延伸，不引入新增品牌规范；如需新增颜色/动效令牌需同步设计库。
- 动效与交互需兼顾桌面与移动视口，遵循当前可达性与键盘操作约束。
- 生成式 UI/工具调用协议保持现有字段（message_id、tool_call_id、uiComponent、actionRequest、reviewConfig），不新增后端字段。

## Success Criteria _(mandatory)_

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: 90% 的可用性测试用户在首次查看对话页时，能在 3 秒内区分人类/AI/工具消息的边界与状态（自述正确率）。
- **SC-002**: 工具卡片详情展开/收起在 0.5 秒内完成且无明显版式跳动；10 次连续操作中无超过 1 次的遮挡或错位。
- **SC-003**: 在包含 5+ 工具调用与长 Markdown 的对话中，滚动与阅读无阻塞；95% 的代码块在桌面与移动视口下无需横向滚动即可完整阅读主要行（不含超长行）。
- **SC-004**: 任务/文件侧栏在新增内容后 2 次点击以内可定位到对应项，95% 用户在 10 秒内完成；空态/错误态均有明确文案与重试/关闭入口。
- **SC-005**: 审批流中，用户可在 10 秒内完成批准或拒绝一次操作且看到反馈；编辑参数后提交的变更摘要可被 90% 用户正确复述。
- **SC-006**: 设计一致性审查（覆盖消息流、工具卡片、侧栏、弹窗、输入区）一次性通过率 ≥ 95%，无未覆盖的组件残留旧样式。
