#!/usr/bin/env python3
"""
运行所有代码检查和测试
"""

import subprocess
import sys
import os

def run_test_script(test_file):
    """运行测试脚本"""
    print(f"\n🧪 运行测试: {test_file}")
    print("-" * 50)
    
    try:
        result = subprocess.run([sys.executable, test_file], 
                              capture_output=True, text=True, timeout=60)
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        print(f"返回码: {result.returncode}")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ 测试超时")
        return False
    except Exception as e:
        print(f"❌ 运行失败: {e}")
        return False

def main():
    """主函数"""
    print("🚀 运行完整的代码分析和测试")
    print("=" * 70)
    
    tests_to_run = [
        '/deep_code_analysis.py',
        '/code_analysis_test.py'
    ]
    
    results = {}
    
    for test_file in tests_to_run:
        if os.path.exists(test_file):
            results[test_file] = run_test_script(test_file)
        else:
            print(f"⚠️  测试文件不存在: {test_file}")
            results[test_file] = False
    
    # 总结
    print("\n" + "=" * 70)
    print("📊 测试总结:")
    
    all_passed = True
    for test_file, passed in results.items():
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"{os.path.basename(test_file)}: {status}")
        if not passed:
            all_passed = False
    
    print(f"\n总体结果: {'✅ 所有测试通过' if all_passed else '⚠️  部分测试失败'}")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)