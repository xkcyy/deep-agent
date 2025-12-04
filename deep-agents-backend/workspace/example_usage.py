#!/usr/bin/env python3
"""
网站克隆工具使用示例
"""

from website_cloner import DownloadConfig, WebsiteCloner
import os

def example_basic_clone():
    """基本克隆示例"""
    print("=== 基本克隆示例 ===")
    
    config = DownloadConfig(
        base_url="https://example.com",
        output_dir="example_clone",
        max_depth=2,
        max_threads=3,
        delay=1.0
    )
    
    cloner = WebsiteCloner(config)
    cloner.clone()

def example_custom_extensions():
    """自定义文件扩展名示例"""
    print("=== 自定义扩展名示例 ===")
    
    config = DownloadConfig(
        base_url="https://blog.example.com",
        output_dir="blog_clone",
        max_depth=3,
        max_threads=5,
        delay=0.5,
        allowed_extensions={'.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.gif'},
        excluded_extensions={'.pdf', '.zip', '.exe'}
    )
    
    cloner = WebsiteCloner(config)
    cloner.clone()

def example_fast_clone():
    """快速克隆示例"""
    print("=== 快速克隆示例 ===")
    
    config = DownloadConfig(
        base_url="https://docs.example.com",
        output_dir="docs_clone",
        max_depth=2,
        max_threads=10,
        delay=0.1,  # 很短的延迟
        timeout=15
    )
    
    cloner = WebsiteCloner(config)
    cloner.clone()

def example_deep_clone():
    """深度克隆示例"""
    print("=== 深度克隆示例 ===")
    
    config = DownloadConfig(
        base_url="https://small-site.example.com",
        output_dir="deep_clone",
        max_depth=5,  # 更深的层级
        max_threads=3,  # 较少线程避免压力
        delay=2.0,  # 更长的延迟
        follow_robots_txt=True
    )
    
    cloner = WebsiteCloner(config)
    cloner.clone()

def example_api_usage():
    """API使用方式示例"""
    print("=== API使用示例 ===")
    
    # 创建配置
    config = DownloadConfig(
        base_url="https://api-example.com",
        output_dir="api_clone",
        user_agent="CustomBot/1.0 (https://mybot.com)",
        max_depth=1,
        max_threads=2,
        delay=1.0
    )
    
    # 创建克隆器实例
    cloner = WebsiteCloner(config)
    
    # 手动添加要下载的URL
    cloner.url_queue.append({
        'url': 'https://api-example.com/page1.html',
        'depth': 0,
        'referrer': None
    })
    
    # 开始克隆
    cloner.clone()
    
    # 获取统计信息
    print(f"成功下载: {len(cloner.downloaded_urls)} 个文件")
    print(f"失败下载: {len(cloner.failed_urls)} 个文件")

if __name__ == "__main__":
    print("网站克隆工具使用示例")
    print("请根据需要运行相应的示例函数")
    print()
    print("可用示例:")
    print("1. example_basic_clone() - 基本克隆")
    print("2. example_custom_extensions() - 自定义扩展名")
    print("3. example_fast_clone() - 快速克隆")
    print("4. example_deep_clone() - 深度克隆")
    print("5. example_api_usage() - API使用")
    print()
    print("注意：请将示例中的URL替换为实际要克隆的网站")
    
    # 取消注释下面一行来运行基本示例
    # example_basic_clone()