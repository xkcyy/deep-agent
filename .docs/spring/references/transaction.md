# Spring 事务管理

> Spring Framework 事务传播机制与配置。

## 事务注解

使用 `@Transactional` 声明事务：

```java
@Service
public class UserService {
    
    @Transactional
    public void createUser(User user) {
        userRepository.save(user);
    }
}
```

## 传播机制

| 传播类型 | 说明 |
|---------|------|
| REQUIRED | 默认，加入当前事务或创建新事务 |
| REQUIRES_NEW | 始终创建新事务 |
| NESTED | 嵌套事务 |
| SUPPORTS | 有事务则加入，无则非事务执行 |

## 隔离级别

```java
@Transactional(isolation = Isolation.READ_COMMITTED)
public void updateUser(User user) {
    // ...
}
```

## 回滚规则

```java
@Transactional(rollbackFor = Exception.class)
public void riskyOperation() throws Exception {
    // ...
}
```

