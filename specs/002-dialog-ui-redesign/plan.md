# Implementation Plan: Dialog UI Redesign

**Branch**: `002-dialog-ui-redesign` | **Date**: 2025-12-09 | **Spec**: `specs/002-dialog-ui-redesign/spec.md`  
**Input**: Feature specification from `/specs/002-dialog-ui-redesign/spec.md`

## Summary

为对话页的所有相关组件提供统一且动态的 UI 设计，不再依赖单一折叠面板模式；针对消息流、工具调用（含生成式 UI、审批）、任务/文件区、线程列表、配置/文件弹窗与输入区分别定义观感、层级、状态与动效，确保可读性、可信度与多上下文协作体验。

## Technical Context

**Language/Version**: TypeScript, React (Next.js 13+/App Router)  
**Primary Dependencies**: Next.js, Tailwind/shadcn UI、lucide-react、@langchain/langgraph-sdk (含 react-ui)  
**Storage**: N/A（前端状态与后端流接口）  
**Testing**: 待确认视觉/交互回归方案（NEEDS CLARIFICATION: 是否需 Playwright 视觉回归）；可用现有前端测试栈补充交互冒烟用例。  
**Target Platform**: Web（桌面优先，兼顾窄屏）  
**Project Type**: Web 前端（monorepo 内 `deep-agents-ui/`）  
**Performance Goals**: 60fps 级别交互，展开/收起 <500ms，无明显布局抖动。  
**Constraints**: 需保持响应式与键盘可达性；状态色/徽章与现有主题一致；生成式 UI 不可阻塞消息阅读。  
**Scale/Scope**: 针对对话页组件集合（ChatInterface、ChatMessage、ToolCallBox、ToolApprovalInterrupt、TasksFilesSidebar、ThreadList、ConfigDialog、FileViewDialog、MarkdownContent、SubAgent flows 等）。

## Constitution Check

Constitution 文件为空模板，未定义具体原则/门禁；当前无阻塞性约束，视为通过。后续若补充正式条款需复查。

## Project Structure

### Documentation (this feature)

```text
specs/002-dialog-ui-redesign/
├── plan.md              # 本文件
├── research.md          # Phase 0 输出
├── data-model.md        # Phase 1 输出
├── quickstart.md        # Phase 1 输出
├── contracts/           # Phase 1 输出
└── tasks.md             # 由 /speckit.tasks 生成
```

### Source Code (repository root, relevant to this feature)

```text
deep-agents-ui/
├── src/app/components/
│   ├── ChatInterface.tsx
│   ├── ChatMessage.tsx
│   ├── ToolCallBox.tsx
│   ├── ToolApprovalInterrupt.tsx
│   ├── TasksFilesSidebar.tsx
│   ├── ThreadList.tsx
│   ├── ConfigDialog.tsx
│   ├── FileViewDialog.tsx
│   ├── MarkdownContent.tsx
│   └── SubAgentIndicator.tsx (plus tool-panels/*)
├── src/providers/ChatProvider.tsx
├── src/app/hooks/useChat.ts
├── src/app/types/types.ts
└── src/app/utils/utils.ts
```

**Structure Decision**: 单体 Web 前端项目（Next.js）；仅在 `deep-agents-ui` 组件层与样式层交付 UI 设计与交互优化，不触达后端。

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
| --------- | ---------- | ------------------------------------ |
| None      | N/A        | N/A                                  |
