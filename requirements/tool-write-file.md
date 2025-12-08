# 需求：文件写入（write_file）UI

## 目标风格
- 暗色渐变 + 霓虹描边卡片，顶部状态条；强调模式与安全感。
- 紧凑信息密度：路径/模式/统计优先，Diff/预览次之。

## 布局
- 头部：图标 + “写入：路径”，模式彩色胶囊（append/overwrite），状态徽标 + 顶部状态条。
- 统计行：字节/行数/checksum，用浅底胶囊展示。
- 变更展示：`diff` 与 `preview` 双槽卡片，霓虹描边，240~300px 滚动。
- 空/等待：提示“已写入/等待返回更多信息…”。
- 错误：红色轻提示，可折叠。

## 状态与交互
- pending/streaming：顶部色条 + 小骨架；保持可折叠。
- completed：显示统计、diff/preview；覆盖模式需提示“覆盖风险”标签；append 显示“追加”标签。
- error/interrupted：保留已返信息，提示可重试（若有回调）。
- 折叠：面板右上角 chevron，记忆展开；diff/预览可单独滚动。

## 数据映射
- 路径优先级：`result.path` > `args.path` > `args.filepath` > `args.file_path` > `args.target` > `args.dst`，缺失用“(未返回路径)”.
- 模式：`args.mode` 或 `result.mode`，默认 overwrite。
- 统计：`bytes`, `lines`, `checksum`；变更：`diff`；内容：`preview`。
- 解析失败：原始文本截断展示。

## 视觉细节
- 紧凑 padding（p-2~p-3），圆角 md，阴影轻；hover 仅边框高亮。
- 标签：模式标签用浅底深字；状态条随状态变色。
- 文本：标题 14px 粗；正文 12px；说明 11px。


