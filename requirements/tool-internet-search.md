# 需求：网络搜索（internet_search）UI

## 目标风格
- 暗色渐变卡片网格（1–2 列自适应），轻阴影 + 霓虹描边；hover 微上浮 0.5px。
- 信息密度高，标题/域名/时间/摘要分区清晰；关键词高亮。

## 布局
- 头部：工具名 + 查询词 + 状态徽标；顶部状态色条（pending 主色、error 红、interrupted 橙、completed 绿）。
- 结果区：1–2 列卡片网格（最多前 10 条），卡片含标题、域名/时间、摘要，右上可放相关度/耗时徽标。
- 空/等待：骨架 shimmer（标题 + 2 行摘要）；无结果提示“等待返回/暂无结果 + 原始截断”。
- 错误：红色轻提示条，可折叠详情。

## 状态与交互
- pending/streaming：骨架 + 已返回项混排；可选自动滚动至最新。
- completed：显示结果数/耗时；允许排序（时间/相关度）与域名过滤（可后续补）。
- error：显示错误文本，保持折叠/展开；提供重试入口（若有）。
- 链接：标题点击外链，新窗口；可选“复制摘要合集”。
- 折叠：面板右上角 chevron，记忆展开状态。

## 数据映射
- 输入 args：`query`, `max_results`, `topic`, `include_raw_content`。
- 输出 result：优先解析 `results|data|items` 数组；字段 `title|url|snippet|content|source|score|published_date`；域名由 url 提取。
- 解析失败：回退文本显示，截断 140+…。

## 视觉细节
- 标题 14px 加粗；摘要 12px；来源 11px 次要色。
- 卡片圆角 md，边框轻；hover 阴影与主色边框。
- 关键词高亮颜色沿用主题 primary。


