# Quickstart: Dialog UI Redesign

1) 获取分支  
- `git checkout 002-dialog-ui-redesign`

2) 安装与运行前端  
- `cd deep-agents-ui`  
- `pnpm install`（或现有包管理器）  
- `pnpm dev` 查看 UI，重点路径：`src/app/components/*`

3) 设计落地范围（按组件而非单折叠面板）  
- 消息流：`ChatInterface`, `ChatMessage`, `MarkdownContent`, `SubAgentIndicator`  
- 工具卡片：`ToolCallBox`（含生成式 UI / 专用 panel / 回退）、`ToolApprovalInterrupt`  
- 任务/文件：`TasksFilesSidebar`, `FilesPopover`, `FileViewDialog`  
- 线程/配置：`ThreadList`, `ConfigDialog`  
- 输入与控制：`ChatInterface` 表单、滚动、状态条

4) 设计要点  
- 分组件卡片化呈现，状态徽章+摘要+可展开详情；中断/错误显式标识。  
- 轻量动效 200–300ms，保持 60fps；可达性与焦点态保留。  
- Markdown/代码块断行与溢出处理；窄屏响应式切换。  
- 任务/文件/线程侧栏保持计数徽章、分组、空/错态提示，不遮挡消息流。

5) 验收对照（摘自 Success Criteria）  
- 3 秒内区分消息类型；工具展开/收起 <0.5s 无抖动。  
- 长对话/多工具下滚动顺畅，代码块可读。  
- 任务/文件 2 次点击内可定位；审批 10 秒内完成并有反馈。  
- 设计一致性审查覆盖所有列举组件。

6) 交付与测试建议  
- 添加 Story/Playground 便于视觉审核；视需要补充 Playwright 视觉/交互冒烟。  
- Dark/Light 主题下对比度与动画一致性检查。

