# Research: Dialog UI Redesign

## Decisions

### 1) 消息流与可读性
- **Decision**: 人类/AI/工具/子代理使用分层卡片+对齐区分，AI/工具左对齐，人类右对齐；保留统一行高与最大宽度，代码块/表格支持换行与水平滚动降级。  
- **Rationale**: 当前 ChatMessage 已按类型分流，需强化层级与阅读节奏，避免单一折叠面板破坏流畅性。  
- **Alternatives considered**: 纯气泡（在长 Markdown 下易溢出）；全宽块状（区分度弱）。

### 2) 工具卡片（含生成式 UI/审批）
- **Decision**: ToolCallBox 采用卡片+状态徽章+摘要行，展开区按优先级显示：生成式 UI > 审批表单 > 专用视图 > 回退参数/结果；支持中断/错误色条与重试指示。  
- **Rationale**: 避免统一折叠面板，保持工具独立可视与可操作性；与当前三态分支契合。  
- **Alternatives considered**: 仅摘要 + 详情弹窗（操作成本高）；全展开（占屏且无层级）。

### 3) 任务/文件与线程侧栏
- **Decision**: 侧栏使用分段标题+计数徽章+分组列表，默认精简高度，可配置自动展开；过渡动效 200–300ms，确保不遮挡消息流。  
- **Rationale**: 满足“每个组件独立展示”而非单折叠，保持多上下文可视。  
- **Alternatives considered**: 单一折叠大面板（不符合需求）；悬浮抽屉（易遮挡消息）。

### 4) 弹窗与遮罩
- **Decision**: ConfigDialog、FileViewDialog 使用一致的圆角/阴影/遮罩透明度；标题/行动区与主体分隔，保持焦点与可达性。  
- **Rationale**: 提升一致性与可读性，关闭后恢复原滚动。  
- **Alternatives considered**: 全屏遮罩（移动端可行但桌面占屏过大）。

### 5) 动效与状态
- **Decision**: 展开/收起、状态切换使用 200–300ms 过渡；状态徽章颜色与现有主题 token 保持；中断/错误态显式色条。  
- **Rationale**: 满足“美观、动态”要求且不引入眩光。  
- **Alternatives considered**: 无动效（缺乏动感）；重动画（易干扰阅读）。

### 6) 可达性与响应式
- **Decision**: 所有可交互元素保留键盘焦点态；文本对比度遵循现有主题；窄屏下消息区与侧栏改为堆叠/可切换视图。  
- **Rationale**: 保证可用性与兼容性。  
- **Alternatives considered**: 仅桌面优化（不满足移动场景）。

## Open Items
- 视觉回归/交互测试方案待确认（如 Playwright + screenshot 基线）。  
- 若需新增设计令牌（颜色/动效），需与设计库同步流程。  
- 移动端最小断点与具体折叠策略可在设计稿中细化。  

## Summary
研究确认：分组件卡片化 + 状态化 + 轻量动效是主轴；折叠模式仅用于局部摘要，不作为全局唯一呈现方式；需保持响应式与可达性。 No blocking unknowns beyond测试工具选择。***

