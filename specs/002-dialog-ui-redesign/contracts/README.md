# Contracts: Dialog UI Redesign

Scope is前端 UI/交互层，无新增后端 API。现有 LangGraph 流接口与 ui/action_request/review_config 协议保持不变。

## Notes
- 前端仅消费现有流事件：messages、values.todos、values.files、values.ui、interrupt。  
- 生成式 UI (`uiComponent`) 与审批 (`actionRequest`/`reviewConfig`) 按既有字段渲染，无字段新增。  
- 若未来需扩展状态/颜色/动画配置，可通过前端常量或主题令牌完成，不引入服务端契约。

