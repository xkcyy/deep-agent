# Spring Boot 快速开始

> Spring Boot 项目搭建指南。

## 创建项目

使用 Spring Initializr 创建项目：

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web,jpa \
  -d type=maven-project \
  -o demo.zip
```

## 项目结构

```
src/
├── main/
│   ├── java/
│   │   └── com/example/demo/
│   │       └── DemoApplication.java
│   └── resources/
│       └── application.yml
└── test/
```

## 启动应用

```java
@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

## 配置文件

```yaml
# application.yml
server:
  port: 8080

spring:
  datasource:
    url: jdbc:h2:mem:testdb
```

