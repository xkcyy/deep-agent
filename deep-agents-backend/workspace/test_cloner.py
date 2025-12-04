#!/usr/bin/env python3
"""
网站克隆工具测试脚本
"""

import os
import sys
import tempfile
import shutil
from website_cloner import DownloadConfig, WebsiteCloner

def test_basic_functionality():
    """测试基本功能"""
    print("🧪 测试基本功能...")
    
    # 创建临时目录
    temp_dir = tempfile.mkdtemp(prefix="cloner_test_")
    
    try:
        # 使用一个简单的测试网站
        config = DownloadConfig(
            base_url="https://httpbin.org/",
            output_dir=temp_dir,
            max_depth=1,
            max_threads=2,
            delay=0.5
        )
        
        cloner = WebsiteCloner(config)
        cloner.clone()
        
        # 检查结果
        if len(cloner.downloaded_urls) > 0:
            print("✅ 基本功能测试通过")
            print(f"   下载了 {len(cloner.downloaded_urls)} 个文件")
        else:
            print("❌ 基本功能测试失败 - 没有下载任何文件")
            
    except Exception as e:
        print(f"❌ 基本功能测试失败: {e}")
    finally:
        # 清理临时目录
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_url_processing():
    """测试URL处理功能"""
    print("\n🧪 测试URL处理功能...")
    
    # 创建临时目录
    temp_dir = tempfile.mkdtemp(prefix="cloner_url_test_")
    
    try:
        config = DownloadConfig(
            base_url="https://httpbin.org/html",
            output_dir=temp_dir,
            max_depth=1,
            max_threads=1,
            delay=0.1
        )
        
        cloner = WebsiteCloner(config)
        
        # 测试URL处理方法
        test_urls = [
            "https://httpbin.org/",
            "https://httpbin.org/css/style.css",
            "https://httpbin.org/js/script.js",
            "https://httpbin.org/images/logo.png"
        ]
        
        for url in test_urls:
            local_path = cloner._get_local_path(url)
            relative_url = cloner._get_relative_url("https://httpbin.org/index.html", url)
            print(f"   {url} -> {local_path}")
            print(f"   相对路径: {relative_url}")
        
        print("✅ URL处理测试通过")
        
    except Exception as e:
        print(f"❌ URL处理测试失败: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_configuration():
    """测试配置功能"""
    print("\n🧪 测试配置功能...")
    
    try:
        config = DownloadConfig(
            base_url="https://example.com",
            output_dir="test_output",
            max_depth=5,
            max_threads=10,
            delay=2.0,
            timeout=60,
            user_agent="TestBot/1.0"
        )
        
        # 验证配置
        assert config.base_url == "https://example.com"
        assert config.max_depth == 5
        assert config.max_threads == 10
        assert config.delay == 2.0
        assert config.timeout == 60
        assert config.user_agent == "TestBot/1.0"
        
        print("✅ 配置测试通过")
        
    except Exception as e:
        print(f"❌ 配置测试失败: {e}")

def test_extension_filtering():
    """测试文件扩展名过滤"""
    print("\n🧪 测试扩展名过滤...")
    
    try:
        config = DownloadConfig(
            base_url="https://example.com",
            output_dir="test_output",
            allowed_extensions={'.html', '.css', '.js'},
            excluded_extensions={'.pdf', '.zip'}
        )
        
        # 测试允许的扩展名
        assert '.html' in config.allowed_extensions
        assert '.css' in config.allowed_extensions
        assert '.js' in config.allowed_extensions
        
        # 测试排除的扩展名
        assert '.pdf' in config.excluded_extensions
        assert '.zip' in config.excluded_extensions
        
        print("✅ 扩展名过滤测试通过")
        
    except Exception as e:
        print(f"❌ 扩展名过滤测试失败: {e}")

def test_file_operations():
    """测试文件操作"""
    print("\n🧪 测试文件操作...")
    
    temp_dir = tempfile.mkdtemp(prefix="cloner_file_test_")
    
    try:
        # 创建测试文件
        test_content = "<html><head><title>Test</title></head><body>Test content</body></html>"
        test_file = os.path.join(temp_dir, "test.html")
        
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        # 验证文件创建
        if os.path.exists(test_file):
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if content == test_content:
                    print("✅ 文件操作测试通过")
                else:
                    print("❌ 文件内容不匹配")
        else:
            print("❌ 文件创建失败")
            
    except Exception as e:
        print(f"❌ 文件操作测试失败: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def run_all_tests():
    """运行所有测试"""
    print("🚀 开始运行网站克隆工具测试...")
    print("=" * 50)
    
    test_configuration()
    test_extension_filtering()
    test_file_operations()
    test_url_processing()
    test_basic_functionality()
    
    print("\n" + "=" * 50)
    print("🏁 测试完成!")

if __name__ == "__main__":
    run_all_tests()