# 系统架构

> 本项目整体架构设计。

## 架构概览

本项目采用分层架构：

```
┌─────────────────────────────────┐
│          Presentation           │
│       (API / Controller)        │
├─────────────────────────────────┤
│           Application           │
│          (Use Cases)            │
├─────────────────────────────────┤
│            Domain               │
│     (Entities / Services)       │
├─────────────────────────────────┤
│         Infrastructure          │
│    (Database / External API)    │
└─────────────────────────────────┘
```

## 技术栈

- **后端**: Spring Boot 3.x
- **LLM 编排**: LangGraph
- **数据库**: PostgreSQL
- **缓存**: Redis

## 模块划分

| 模块 | 职责 |
|------|------|
| `api` | REST API 接口层 |
| `service` | 业务逻辑层 |
| `domain` | 领域模型 |
| `infra` | 基础设施层 |

