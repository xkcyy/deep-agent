#!/usr/bin/env python3
"""
网站克隆工具 - Website Cloner (修复版本)
功能：下载完整网站的静态资源，支持离线浏览

作者：AI Assistant
版本：1.0.1
"""

import os
import sys
import time
import re
from urllib.parse import urljoin, urlparse, unquote
from urllib.robotparser import RobotFileParser
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Set, Dict, List, Optional
import argparse
import logging
import threading
from queue import Queue

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("请安装必要的依赖：pip install requests beautifulsoup4")
    sys.exit(1)


@dataclass
class DownloadConfig:
    """下载配置类"""
    base_url: str
    output_dir: str
    max_depth: int = 3
    max_threads: int = 5
    delay: float = 1.0
    timeout: int = 30
    user_agent: str = "WebsiteCloner/1.0"
    follow_robots_txt: bool = True
    allowed_extensions: Set[str] = None
    excluded_extensions: Set[str] = None
    
    def __post_init__(self):
        if self.allowed_extensions is None:
            self.allowed_extensions = {
                '.html', '.htm', '.css', '.js', '.json', '.xml',
                '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico',
                '.woff', '.woff2', '.ttf', '.eot',
                '.pdf', '.doc', '.docx', '.txt'
            }
        if self.excluded_extensions is None:
            self.excluded_extensions = set()


class WebsiteCloner:
    """网站克隆器主类"""
    
    def __init__(self, config: DownloadConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': config.user_agent})
        
        # 设置日志 - 只在首次时配置
        self._setup_logging()
        
        # 线程安全的状态跟踪
        self.downloaded_urls: Set[str] = set()
        self.failed_urls: Set[str] = set()
        self.url_queue = Queue()
        self.domain_filter = self._get_domain_filter()
        
        # 线程锁
        self._lock = threading.Lock()
        
        # 创建输出目录
        self._create_output_directory()
        
        # 机器人文件检查
        self.robots_parser = None
        if config.follow_robots_txt:
            self._setup_robots_parser()
    
    def _setup_logging(self):
        """设置日志配置 - 线程安全"""
        # 只配置一次，避免重复调用
        if not logging.getLogger().handlers:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler(os.path.join(self.config.output_dir, 'cloner.log')),
                    logging.StreamHandler()
                ]
            )
        self.logger = logging.getLogger(__name__)
    
    def _get_domain_filter(self) -> str:
        """获取域名过滤器"""
        parsed = urlparse(self.config.base_url)
        return f"{parsed.scheme}://{parsed.netloc}"
    
    def _create_output_directory(self):
        """创建输出目录"""
        if not os.path.exists(self.config.output_dir):
            os.makedirs(self.config.output_dir, exist_ok=True)
            if hasattr(self, 'logger'):
                self.logger.info(f"创建输出目录: {self.config.output_dir}")
    
    def _setup_robots_parser(self):
        """设置robots.txt解析器"""
        try:
            robots_url = urljoin(self.config.base_url, '/robots.txt')
            response = self.session.get(robots_url, timeout=self.config.timeout)
            if response.status_code == 200:
                self.robots_parser = RobotFileParser()
                self.robots_parser.set_url(robots_url)
                self.robots_parser.parse(response.text.splitlines())
                self.logger.info("已加载robots.txt规则")
        except Exception as e:
            self.logger.warning(f"无法加载robots.txt: {e}")
    
    def _is_allowed_by_robots(self, url: str) -> bool:
        """检查URL是否被robots.txt允许"""
        if not self.robots_parser:
            return True
        return self.robots_parser.can_fetch(self.config.user_agent, url)
    
    def _get_local_path(self, url: str) -> str:
        """获取本地文件路径"""
        parsed = urlparse(url)
        path = parsed.path
        
        # 处理路径
        if path.endswith('/'):
            path += 'index.html'
        elif not os.path.splitext(path)[1]:
            path += '/index.html'
        
        # URL解码
        path = unquote(path)
        
        # 移除开头的斜杠
        path = path.lstrip('/')
        
        return os.path.join(self.config.output_dir, path)
    
    def _get_relative_url(self, current_url: str, target_url: str) -> str:
        """获取相对URL路径"""
        current_path = self._get_local_path(current_url)
        target_path = self._get_local_path(target_url)
        
        # 计算相对路径
        current_dir = os.path.dirname(current_path)
        target_dir = os.path.dirname(target_path)
        target_filename = os.path.basename(target_path)
        
        # 获取相对路径
        try:
            relative_path = os.path.relpath(os.path.join(target_dir, target_filename), current_dir)
            return relative_path.replace('\\', '/')
        except ValueError:
            # 如果无法计算相对路径，返回绝对路径
            return target_path
    
    def _should_download_url(self, url: str, depth: int) -> bool:
        """判断是否应该下载URL - 线程安全"""
        with self._lock:
            if url in self.downloaded_urls or url in self.failed_urls:
                return False
        
        if depth > self.config.max_depth:
            return False
        
        # 检查域名
        if not url.startswith(self.domain_filter):
            return False
        
        # 检查文件扩展名
        file_ext = os.path.splitext(urlparse(url).path)[1].lower()
        if file_ext and file_ext not in self.config.allowed_extensions:
            return False
        
        if file_ext in self.config.excluded_extensions:
            return False
        
        # 检查robots.txt
        if not self._is_allowed_by_robots(url):
            return False
        
        return True
    
    def _download_file(self, url: str, local_path: str) -> bool:
        """下载单个文件"""
        try:
            response = self.session.get(url, timeout=self.config.timeout)
            response.raise_for_status()
            
            # 创建目录
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            # 写入文件
            with open(local_path, 'wb') as f:
                f.write(response.content)
            
            self.logger.info(f"下载完成: {url} -> {local_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"下载失败 {url}: {e}")
            return False
    
    def _process_html(self, html_content: str, base_url: str, depth: int) -> str:
        """处理HTML内容，转换链接"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 处理各种标签的URL
        url_tags = {
            'a': 'href',
            'link': 'href',
            'script': 'src',
            'img': 'src',
            'iframe': 'src',
            'source': 'src',
            'video': 'src',
            'audio': 'src',
            'embed': 'src',
            'object': 'data'
        }
        
        for tag_name, attr in url_tags.items():
            for tag in soup.find_all(tag_name):
                if tag.has_attr(attr):
                    original_url = tag[attr]
                    absolute_url = urljoin(base_url, original_url)
                    
                    if self._should_download_url(absolute_url, depth + 1):
                        # 添加到下载队列 - 线程安全
                        self.url_queue.put({
                            'url': absolute_url,
                            'depth': depth + 1,
                            'referrer': base_url
                        })
                        
                        # 转换为相对路径
                        try:
                            relative_url = self._get_relative_url(base_url, absolute_url)
                            tag[attr] = relative_url
                        except (ValueError, OSError) as e:
                            self.logger.debug(f"无法转换相对路径 {absolute_url}: {e}")
                            # 保持原始URL
                            pass
        
        # 处理CSS中的URL
        for style in soup.find_all('style'):
            if style.string:
                style.string = self._process_css_urls(style.string, base_url, depth)
        
        for tag in soup.find_all(attrs={'style': True}):
            tag['style'] = self._process_css_urls(tag['style'], base_url, depth)
        
        return str(soup)
    
    def _process_css_urls(self, css_content: str, base_url: str, depth: int) -> str:
        """处理CSS中的URL"""
        url_pattern = re.compile(r'url\(["\']?(.*?)["\']?\)', re.IGNORECASE)
        
        def replace_url(match):
            original_url = match.group(1)
            if original_url.startswith('data:') or original_url.startswith('#'):
                return match.group(0)
            
            absolute_url = urljoin(base_url, original_url)
            
            if self._should_download_url(absolute_url, depth + 1):
                # 添加到下载队列 - 线程安全
                self.url_queue.put({
                    'url': absolute_url,
                    'depth': depth + 1,
                    'referrer': base_url
                })
                
                try:
                    relative_url = self._get_relative_url(base_url, absolute_url)
                    return f'url({relative_url})'
                except (ValueError, OSError) as e:
                    self.logger.debug(f"无法转换CSS相对路径 {absolute_url}: {e}")
                    return match.group(0)
            
            return match.group(0)
        
        return url_pattern.sub(replace_url, css_content)
    
    def _download_and_process_url(self, url_info: Dict) -> bool:
        """下载并处理单个URL"""
        url = url_info['url']
        depth = url_info['depth']
        
        # 双重检查 - 线程安全
        with self._lock:
            if url in self.downloaded_urls:
                return True
        
        try:
            self.logger.info(f"正在下载: {url} (深度: {depth})")
            
            response = self.session.get(url, timeout=self.config.timeout)
            response.raise_for_status()
            
            local_path = self._get_local_path(url)
            
            # 创建目录
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            # 处理HTML文件
            content_type = response.headers.get('content-type', '').lower()
            if 'text/html' in content_type:
                processed_content = self._process_html(response.text, url, depth)
                with open(local_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
            else:
                # 其他文件类型直接保存
                with open(local_path, 'wb') as f:
                    f.write(response.content)
            
            # 添加到已下载集合 - 线程安全
            with self._lock:
                self.downloaded_urls.add(url)
            
            self.logger.info(f"保存完成: {local_path}")
            
            # 添加延迟
            time.sleep(self.config.delay)
            
            return True
            
        except Exception as e:
            self.logger.error(f"处理失败 {url}: {e}")
            # 添加到失败集合 - 线程安全
            with self._lock:
                self.failed_urls.add(url)
            return False
    
    def clone(self):
        """开始克隆网站"""
        self.logger.info(f"开始克隆网站: {self.config.base_url}")
        self.logger.info(f"输出目录: {self.config.output_dir}")
        
        # 添加起始URL到队列
        self.url_queue.put({
            'url': self.config.base_url,
            'depth': 0,
            'referrer': None
        })
        
        # 处理队列
        processed_count = 0
        with ThreadPoolExecutor(max_workers=self.config.max_threads) as executor:
            while not self.url_queue.empty() and processed_count < 1000:  # 限制总处理数量
                # 获取当前批次的URL
                batch = []
                batch_size = min(self.config.max_threads * 2, self.url_queue.qsize())
                
                for _ in range(batch_size):
                    if not self.url_queue.empty():
                        try:
                            batch.append(self.url_queue.get_nowait())
                        except:
                            break
                
                if not batch:
                    break
                
                # 并行处理
                futures = [executor.submit(self._download_and_process_url, url_info) for url_info in batch]
                
                for future in as_completed(futures):
                    if future.result():
                        processed_count += 1
                
                # 显示进度
                self.logger.info(f"进度: 已处理 {processed_count} 个页面, 队列剩余 {self.url_queue.qsize()} 个URL")
        
        self.logger.info(f"克隆完成! 总共下载 {len(self.downloaded_urls)} 个文件")
        self.logger.info(f"失败 {len(self.failed_urls)} 个文件")
        
        # 生成报告
        self._generate_report()
    
    def _generate_report(self):
        """生成克隆报告"""
        report_path = os.path.join(self.config.output_dir, 'clone_report.txt')
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"网站克隆报告\n")
            f.write(f"=" * 50 + "\n")
            f.write(f"目标网站: {self.config.base_url}\n")
            f.write(f"克隆时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"成功下载: {len(self.downloaded_urls)} 个文件\n")
            f.write(f"失败下载: {len(self.failed_urls)} 个文件\n")
            f.write(f"\n成功下载的URL列表:\n")
            f.write("-" * 30 + "\n")
            for url in sorted(self.downloaded_urls):
                f.write(f"{url}\n")
            
            if self.failed_urls:
                f.write(f"\n失败的URL列表:\n")
                f.write("-" * 30 + "\n")
                for url in sorted(self.failed_urls):
                    f.write(f"{url}\n")
        
        self.logger.info(f"报告已生成: {report_path}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='网站克隆工具')
    parser.add_argument('url', help='要克隆的网站URL')
    parser.add_argument('-o', '--output', default='cloned_website', help='输出目录 (默认: cloned_website)')
    parser.add_argument('-d', '--depth', type=int, default=3, help='最大下载深度 (默认: 3)')
    parser.add_argument('-t', '--threads', type=int, default=5, help='下载线程数 (默认: 5)')
    parser.add_argument('--delay', type=float, default=1.0, help='请求间隔秒数 (默认: 1.0)')
    parser.add_argument('--timeout', type=int, default=30, help='请求超时秒数 (默认: 30)')
    parser.add_argument('--no-robots', action='store_true', help='忽略robots.txt规则')
    parser.add_argument('--user-agent', default='WebsiteCloner/1.0', help='User-Agent字符串')
    
    args = parser.parse_args()
    
    # 创建配置
    config = DownloadConfig(
        base_url=args.url,
        output_dir=args.output,
        max_depth=args.depth,
        max_threads=args.threads,
        delay=args.delay,
        timeout=args.timeout,
        user_agent=args.user_agent,
        follow_robots_txt=not args.no_robots
    )
    
    # 开始克隆
    try:
        cloner = WebsiteCloner(config)
        cloner.clone()
        print(f"\n✅ 网站克隆完成! 请查看 {config.output_dir} 目录")
    except KeyboardInterrupt:
        print("\n⚠️  用户中断操作")
    except Exception as e:
        print(f"\n❌ 克隆失败: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()