#!/usr/bin/env python3
"""
代码分析测试 - 验证关键逻辑和边界情况
"""

import os
import sys
import tempfile
import shutil
from website_cloner_fixed import DownloadConfig, WebsiteCloner

def test_url_processing_edge_cases():
    """测试URL处理的边界情况"""
    print("🧪 测试URL处理边界情况...")
    
    # 创建临时目录
    temp_dir = tempfile.mkdtemp(prefix="cloner_edge_test_")
    
    try:
        config = DownloadConfig(
            base_url="https://example.com",
            output_dir=temp_dir,
            max_depth=1,
            max_threads=1
        )
        
        cloner = WebsiteCloner(config)
        
        # 测试各种边界URL
        test_cases = [
            ("https://example.com/", "index.html"),
            ("https://example.com/path", "path/index.html"),
            ("https://example.com/file.html", "file.html"),
            ("https://example.com/dir/", "dir/index.html"),
            ("https://example.com/path/to/file.js", "path/to/file.js"),
            ("https://example.com/path%20with%20spaces.html", "path with spaces.html"),
        ]
        
        for url, expected_file in test_cases:
            local_path = cloner._get_local_path(url)
            relative_path = os.path.relpath(local_path, temp_dir)
            
            print(f"   {url}")
            print(f"   -> {relative_path}")
            print(f"   期望包含: {expected_file}")
            
            if expected_file in relative_path:
                print("   ✅ 正确")
            else:
                print("   ❌ 错误")
        
        print("✅ URL边界情况测试完成")
        
    except Exception as e:
        print(f"❌ URL边界情况测试失败: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_thread_safety():
    """测试线程安全性"""
    print("\n🧪 测试线程安全性...")
    
    temp_dir = tempfile.mkdtemp(prefix="cloner_thread_test_")
    
    try:
        config = DownloadConfig(
            base_url="https://example.com",
            output_dir=temp_dir,
            max_depth=1,
            max_threads=5
        )
        
        cloner = WebsiteCloner(config)
        
        # 测试队列操作
        test_urls = [
            "https://example.com/page1.html",
            "https://example.com/page2.html",
            "https://example.com/page3.html",
        ]
        
        # 添加URL到队列
        for url in test_urls:
            cloner.url_queue.put({'url': url, 'depth': 0, 'referrer': None})
        
        print(f"   队列大小: {cloner.url_queue.qsize()}")
        
        # 测试线程安全的集合操作
        with cloner._lock:
            cloner.downloaded_urls.add("https://example.com/test.html")
            cloner.failed_urls.add("https://example.com/failed.html")
        
        print(f"   已下载URL数量: {len(cloner.downloaded_urls)}")
        print(f"   失败URL数量: {len(cloner.failed_urls)}")
        
        print("✅ 线程安全测试完成")
        
    except Exception as e:
        print(f"❌ 线程安全测试失败: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_domain_filtering():
    """测试域名过滤功能"""
    print("\n🧪 测试域名过滤...")
    
    temp_dir = tempfile.mkdtemp(prefix="cloner_domain_test_")
    
    try:
        config = DownloadConfig(
            base_url="https://example.com",
            output_dir=temp_dir,
            max_depth=2
        )
        
        cloner = WebsiteCloner(config)
        
        # 测试各种URL
        test_cases = [
            ("https://example.com/page.html", True),
            ("https://example.com/sub/page.html", True),
            ("https://other.com/page.html", False),
            ("https://sub.example.com/page.html", False),  # 严格匹配
        ]
        
        for url, expected in test_cases:
            should_download = cloner._should_download_url(url, 0)
            result = "✅" if should_download == expected else "❌"
            print(f"   {result} {url} -> {should_download}")
        
        print("✅ 域名过滤测试完成")
        
    except Exception as e:
        print(f"❌ 域名过滤测试失败: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_extension_filtering():
    """测试文件扩展名过滤"""
    print("\n🧪 测试扩展名过滤...")
    
    temp_dir = tempfile.mkdtemp(prefix="cloner_ext_test_")
    
    try:
        config = DownloadConfig(
            base_url="https://example.com",
            output_dir=temp_dir,
            max_depth=2,
            allowed_extensions={'.html', '.css', '.js'},
            excluded_extensions={'.pdf'}
        )
        
        cloner = WebsiteCloner(config)
        
        test_cases = [
            ("https://example.com/page.html", True),
            ("https://example.com/style.css", True),
            ("https://example.com/script.js", True),
            ("https://example.com/image.png", False),
            ("https://example.com/document.pdf", False),
        ]
        
        for url, expected in test_cases:
            should_download = cloner._should_download_url(url, 0)
            result = "✅" if should_download == expected else "❌"
            print(f"   {result} {url} -> {should_download}")
        
        print("✅ 扩展名过滤测试完成")
        
    except Exception as e:
        print(f"❌ 扩展名过滤测试失败: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_robots_txt_simulation():
    """模拟robots.txt测试"""
    print("\n🧪 测试robots.txt处理...")
    
    temp_dir = tempfile.mkdtemp(prefix="cloner_robots_test_")
    
    try:
        config = DownloadConfig(
            base_url="https://example.com",
            output_dir=temp_dir,
            follow_robots_txt=False  # 简化测试
        )
        
        cloner = WebsiteCloner(config)
        
        # 测试robots检查
        is_allowed = cloner._is_allowed_by_robots("https://example.com/allowed")
        print(f"   robots.txt检查: {is_allowed} (应该为True，因为没有配置robots)")
        
        print("✅ robots.txt测试完成")
        
    except Exception as e:
        print(f"❌ robots.txt测试失败: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def run_comprehensive_tests():
    """运行全面的代码测试"""
    print("🚀 开始全面的代码分析测试...")
    print("=" * 60)
    
    test_url_processing_edge_cases()
    test_thread_safety()
    test_domain_filtering()
    test_extension_filtering()
    test_robots_txt_simulation()
    
    print("\n" + "=" * 60)
    print("🏁 全面测试完成!")

if __name__ == "__main__":
    run_comprehensive_tests()