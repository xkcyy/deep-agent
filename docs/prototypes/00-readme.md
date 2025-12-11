# 原型目录说明
- 目的：集中管理产品原型稿、状态与评审记录，对应 `docs/requirements` 的需求编号。
- 命名：两位序号 + 短描述；子目录内首选 `readme.md` 作为入口，引用外部原型链接（Figma/白板）与截图。
- 状态：草稿 / 评审中 / 冻结；在各子目录 readme 顶部标注。
- 版本：同一文件以 v1, v2… 递增；重大改动保留变更记录。

## 目录
- `common/`：通用组件与交互模式原型（输入框、气泡、附件、折叠/抽屉、通知/错误态等）。
- `flows/`：端到端用户旅程原型，按需求编号分目录。
- `widgets/`：可复用部件的多状态原型（如工具卡片、Tab、模型/模板选择器等）。
- `assets/`：原型配色、图标、占位图等素材。
- `reviews/`：评审记录、结论与行动项。

## 对应需求的流程目录（flows）
- `01-login-and-initial-load/`
- `02-conversation-list/`
- `03-chat-input-and-send/`
- `04-session-and-context/`
- `05-tool-registry-and-routing/`
- `06-main-window-and-tabs/`
- `07-resource-manager/`
- `08-model-config-and-switch/`
- `09-prompt-template-management/`
- `10-export-and-copy/`
- `11-conversation-export-backlog/`
- `12-light-observability-and-errors/`
- `13-tool-calls-and-display/`


