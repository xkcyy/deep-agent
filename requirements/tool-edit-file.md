# 需求：文件编辑（edit_file）UI

## 目标风格
- 暗色渐变 + 霓虹描边卡片，顶部状态条；突出差异展示。
- 信息聚焦：路径/统计胶囊，Diff/预览高亮。

## 布局
- 头部：图标 + “编辑：路径”，状态徽标 + 顶部状态条。
- 统计行：字节/行数，用浅底胶囊。
- Diff：霓虹描边文本区，240~300px 滚动，高亮变更标题“变更 Diff”。
- 预览：可选 preview 卡片，独立滚动。
- 空/等待：提示“已编辑/等待返回…”。
- 错误：红色轻提示，可折叠。

## 状态与交互
- pending/streaming：骨架 + 状态条；可折叠。
- completed：展示 Diff/预览；保持紧凑。
- error/interrupted：保留已返信息，提示可重试（若有回调）。
- 折叠：面板右上角 chevron，记忆展开；Diff/预览可滚动。

## 数据映射
- 路径优先级：`result.path` > `args.path` > `args.filepath` > `args.file_path` > `args.target` > `args.dst`，缺失用“(未返回路径)”.
- 统计：`bytes`, `lines`；变更：`diff`；预览：`preview`；错误：`error`。
- 解析失败：原始文本截断展示。

## 视觉细节
- 紧凑 padding（p-2~p-3），圆角 md，阴影轻；hover 仅边框高亮。
- 标题 14px 粗；正文 12px；说明 11px。
- Diff/预览框：边框 + 背景弱色，滚动替代撑高。


