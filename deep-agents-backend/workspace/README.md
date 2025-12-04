# 网站克隆工具 (Website Cloner)

一个功能强大的Python网站克隆工具，可以下载完整网站的静态资源，支持离线浏览。

## ✨ 功能特性

- 🌐 **完整克隆**: 下载HTML、CSS、JavaScript、图片等所有静态资源
- 🔄 **智能链接转换**: 自动转换为本地相对路径，确保离线可用
- ⚡ **多线程下载**: 支持并发下载，提高克隆速度
- 🛡️ **合规性检查**: 遵守robots.txt规则
- 📊 **详细日志**: 完整的下载日志和进度显示
- 📝 **生成报告**: 自动生成克隆报告
- 🎛️ **灵活配置**: 丰富的命令行参数选项

## 🚀 快速开始

### 安装依赖

```bash
pip install requests beautifulsoup4
```

### 基本用法

```bash
# 克隆单个网站
python website_cloner.py https://example.com

# 指定输出目录
python website_cloner.py https://example.com -o my_website

# 设置最大深度和线程数
python website_cloner.py https://example.com -d 2 -t 10
```

## 📖 详细用法

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `url` | 要克隆的网站URL | 必需 |
| `-o, --output` | 输出目录 | `cloned_website` |
| `-d, --depth` | 最大下载深度 | `3` |
| `-t, --threads` | 下载线程数 | `5` |
| `--delay` | 请求间隔秒数 | `1.0` |
| `--timeout` | 请求超时秒数 | `30` |
| `--no-robots` | 忽略robots.txt规则 | `False` |
| `--user-agent` | User-Agent字符串 | `WebsiteCloner/1.0` |

### 使用示例

```bash
# 克隆到指定目录，深度为2层，使用10个线程
python website_cloner.py https://blog.example.com -o my_blog -d 2 -t 10

# 快速克隆（无延迟，更多线程）
python website_cloner.py https://docs.example.com --delay 0.1 -t 15

# 忽略robots.txt规则
python website_cloner.py https://example.com --no-robots

# 自定义User-Agent
python website_cloner.py https://example.com --user-agent "MyBot/1.0"
```

## 🏗️ 技术架构

### 核心组件

1. **配置管理** (`DownloadConfig`)
   - 统一管理所有下载参数
   - 支持文件扩展名过滤

2. **克隆器** (`WebsiteCloner`)
   - 主要的网站克隆逻辑
   - URL队列管理
   - 多线程下载协调

3. **URL处理器**
   - 相对路径转换
   - 链接重写
   - robots.txt检查

### 支持的资源类型

- **网页**: HTML, HTM
- **样式**: CSS
- **脚本**: JavaScript, JSON
- **图片**: PNG, JPG, JPEG, GIF, BMP, SVG, ICO
- **字体**: WOFF, WOFF2, TTF, EOT
- **文档**: PDF, DOC, DOCX, TXT

## 📁 输出结构

克隆后的网站会保持原有的目录结构：

```
cloned_website/
├── index.html              # 首页
├── css/                    # 样式文件
│   └── style.css
├── js/                     # JavaScript文件
│   └── script.js
├── images/                 # 图片文件
│   └── logo.png
├── fonts/                  # 字体文件
└── cloner.log             # 克隆日志
└── clone_report.txt       # 克隆报告
```

## 📊 日志和报告

### 日志文件 (`cloner.log`)
- 实时下载进度
- 成功/失败的URL记录
- 错误信息

### 克隆报告 (`clone_report.txt`)
- 克隆统计信息
- 成功下载的URL列表
- 失败的URL列表

## ⚠️ 注意事项

### 法律和道德
- 遵守目标网站的robots.txt规则
- 尊重版权和知识产权
- 合理使用，避免对目标服务器造成压力

### 技术限制
- 仅支持静态资源下载
- 动态内容（AJAX、API调用）无法克隆
- 需要认证的页面无法访问
- JavaScript渲染的内容无法处理

### 性能建议
- 设置适当的延迟避免被封IP
- 根据网站大小调整线程数
- 监控磁盘空间使用

## 🛠️ 开发和扩展

### 自定义配置

```python
from website_cloner import DownloadConfig, WebsiteCloner

config = DownloadConfig(
    base_url="https://example.com",
    output_dir="my_clone",
    max_depth=5,
    max_threads=8,
    delay=0.5,
    allowed_extensions={'.html', '.css', '.js', '.png', '.jpg'},
    excluded_extensions={'.pdf', '.zip'}
)

cloner = WebsiteCloner(config)
cloner.clone()
```

### 扩展功能

- 添加自定义资源类型支持
- 实现增量更新功能
- 集成代理支持
- 添加内容过滤功能

## 🐛 故障排除

### 常见问题

1. **下载速度慢**
   - 减少延迟时间：`--delay 0.1`
   - 增加线程数：`-t 10`

2. **某些文件无法下载**
   - 检查robots.txt规则
   - 使用 `--no-robots` 跳过检查
   - 检查文件扩展名是否在允许列表中

3. **内存使用过高**
   - 减少线程数：`-t 3`
   - 限制克隆深度：`-d 2`

4. **链接转换错误**
   - 检查原始网站URL格式
   - 确保URL格式正确（包含http://或https://）

## 📄 许可证

MIT License - 详见LICENSE文件

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个工具！

---

**免责声明**: 使用本工具时请遵守相关法律法规和网站的使用条款。作者不对任何因使用本工具而导致的法律问题或技术问题承担责任。