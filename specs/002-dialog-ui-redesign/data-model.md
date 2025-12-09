# Data Model: Dialog UI Redesign

Derived from spec entities (UI/interaction oriented).

## Entities

### Message
- id: string
- type: "human" | "ai" | "tool"
- content: text/markdown/blocks
- tool_calls: ToolCall[] (ai)
- metadata: { message_id?, tool_call_id?, anchors?, ui?: UIBlockRef }

### ToolCall
- id: string
- name: string
- args: record<any>
- status: "pending" | "completed" | "error" | "interrupted"
- result?: string | object
- uiComponent?: UIBlockRef
- actionRequest?: ActionRequest
- reviewConfig?: ReviewConfig

### SubAgent
- id: string
- subagent_type: string
- input: object|string
- output?: object|string
- status: ToolCall.status (inherit)

### TodoItem
- id: string
- content: string
- status: "pending" | "in_progress" | "completed"

### FileItem
- path: string
- content: string
- editable?: boolean (UI-only flag)

### Thread
- id: string
- title: string
- description: string
- status: "idle" | "busy" | "interrupted" | "error"
- updatedAt: datetime

### UIBlockRef
- message_id?: string
- tool_call_id?: string
- id?: string
- metadata?: record<any>

### ActionRequest / ReviewConfig
- actionRequest: { name: string; description?: string; args: record<any> }
- reviewConfig: { allowedDecisions: string[]; actionName: string }

## Relationships
- Message 1..n ToolCall (AI)
- ToolCall 0..1 UIBlockRef
- ToolCall 0..1 ActionRequest/ReviewConfig
- ToolCall 0..n SubAgent (where name == "task" and args.subagent_type)
- Thread 1..n Message
- Thread aggregates TodoItem[], FileItem[]

## State Considerations
- ToolCall status transitions: pending → completed | error | interrupted.
- TodoItem status transitions: pending ↔ in_progress → completed.
- Thread status driven by backend events; UI must reflect interrupted/error distinctly.

## Validation Notes
- Message.tool_calls must include id to bind tool results/ui blocks.
- ToolCall args/result should be JSON-safe for pretty rendering.
- SubAgent requires subagent_type to render indicator; otherwise fallback hides card.
- FileItem path must be non-empty; editing disabled when interrupt/loading.***

