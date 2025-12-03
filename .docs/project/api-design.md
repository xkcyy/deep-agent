# API 设计规范

> 接口设计规范与约定。

## RESTful 规范

### URL 命名

- 使用名词复数: `/users`, `/orders`
- 使用连字符: `/user-profiles`
- 版本号前缀: `/api/v1/users`

### HTTP 方法

| 方法 | 用途 |
|------|------|
| GET | 查询资源 |
| POST | 创建资源 |
| PUT | 全量更新 |
| PATCH | 部分更新 |
| DELETE | 删除资源 |

## 响应格式

```json
{
  "code": 200,
  "message": "success",
  "data": { ... }
}
```

## 错误处理

```json
{
  "code": 400,
  "message": "Validation failed",
  "errors": [
    {"field": "email", "message": "Invalid email format"}
  ]
}
```

## 分页

```
GET /api/v1/users?page=1&size=20
```

