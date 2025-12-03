#!/usr/bin/env python3
"""
文档同步工具 - 将远程文档拉取到本地 .docs/ 目录

支持的站点类型:
- mintlify: Mintlify 文档站点
- llms-txt: llms.txt 标准站点
- github-raw: GitHub 仓库原始文件

使用方法:
    python sync_docs.py                    # 同步所有源
    python sync_docs.py --source langgraph # 同步指定源
    python sync_docs.py --dry-run          # 预览模式
"""

import argparse
import os
import re
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup

try:
    import html2text
except ImportError:
    html2text = None


# ============================================================================
# 数据模型
# ============================================================================

@dataclass
class DocPage:
    """文档页面"""
    url: str
    title: str
    description: str
    relative_path: str  # 相对于 target 的路径
    url_path: str = ""  # 原始 URL 路径，用于过滤
    content: Optional[str] = None


@dataclass
class SourceConfig:
    """文档源配置"""
    name: str
    type: str
    target: str
    base_url: Optional[str] = None
    url: Optional[str] = None
    repo: Optional[str] = None
    branch: str = "main"
    docs_path: Optional[str] = None
    include_patterns: Optional[list] = None
    exclude_patterns: Optional[list] = None
    max_depth: int = 3
    preserve_path: bool = True  # 是否保留 URL 路径结构
    path_prefix: Optional[str] = None  # URL 路径前缀，用于截取相对路径


# ============================================================================
# 解析器基类
# ============================================================================

class DocParser(ABC):
    """文档解析器基类"""
    
    def __init__(self, config: SourceConfig, dry_run: bool = False):
        self.config = config
        self.dry_run = dry_run
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; DocSync/1.0)'
        })
    
    @abstractmethod
    def fetch_index(self) -> list[DocPage]:
        """获取文档索引"""
        pass
    
    @abstractmethod
    def fetch_content(self, page: DocPage) -> str:
        """获取页面内容并转换为 Markdown"""
        pass
    
    def sync(self) -> list[DocPage]:
        """执行同步"""
        print(f"\n{'='*60}")
        print(f"同步源: {self.config.name} ({self.config.type})")
        print(f"目标目录: {self.config.target}")
        print(f"{'='*60}")
        
        # 获取索引
        pages = self.fetch_index()
        print(f"发现 {len(pages)} 个文档页面")
        
        # 过滤
        pages = self._filter_pages(pages)
        print(f"过滤后 {len(pages)} 个页面")
        
        if self.dry_run:
            print("\n[预览模式] 将下载以下文件:")
            for page in pages:
                print(f"  - {page.relative_path}: {page.title}")
            return pages
        
        # 下载并保存
        synced = []
        for i, page in enumerate(pages, 1):
            print(f"[{i}/{len(pages)}] {page.title}...", end=" ")
            try:
                content = self.fetch_content(page)
                self._save_page(page, content)
                synced.append(page)
                print("✓")
            except Exception as e:
                print(f"✗ ({e})")
        
        # 生成索引
        self._generate_llms_txt(synced)
        
        return synced
    
    def _filter_pages(self, pages: list[DocPage]) -> list[DocPage]:
        """根据 include/exclude 模式过滤页面"""
        result = []
        for page in pages:
            # 使用 url_path (原始 URL 路径) 进行过滤，如果没有则使用 relative_path
            path = page.url_path if page.url_path else page.relative_path
            
            # 检查 include
            if self.config.include_patterns:
                if not any(self._match_pattern(path, p) for p in self.config.include_patterns):
                    continue
            
            # 检查 exclude
            if self.config.exclude_patterns:
                if any(self._match_pattern(path, p) for p in self.config.exclude_patterns):
                    continue
            
            result.append(page)
        return result
    
    def _match_pattern(self, path: str, pattern: str) -> bool:
        """简单的通配符匹配"""
        import fnmatch
        return fnmatch.fnmatch(path, pattern)
    
    def _save_page(self, page: DocPage, content: str):
        """保存页面到文件"""
        target_path = Path(self.config.target) / page.relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 添加 frontmatter
        frontmatter = f"# {page.title}\n\n"
        if page.description:
            frontmatter += f"> {page.description}\n\n"
        frontmatter += f"> Source: {page.url}\n\n"
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + content)
    
    def _generate_llms_txt(self, pages: list[DocPage]):
        """生成 llms.txt 索引文件，按目录层级分组"""
        target_dir = Path(self.config.target)
        llms_path = target_dir / "llms.txt"
        
        # 按目录分组
        groups: dict[str, list[tuple[str, DocPage]]] = {}
        
        for page in pages:
            # 获取目录路径
            path_parts = Path(page.relative_path).parts
            if len(path_parts) > 1:
                # 有子目录，使用第一级目录作为分组
                group_name = path_parts[0].replace('-', ' ').replace('_', ' ').title()
            else:
                # 根目录文件
                group_name = "Overview"
            
            if group_name not in groups:
                groups[group_name] = []
            groups[group_name].append((page.relative_path, page))
        
        content = f"# {self.config.name.replace('-', ' ').title()} Documentation\n\n"
        content += f"> Synced from: {self.config.base_url or self.config.url or self.config.repo}\n\n"
        
        # 按分组输出，优先显示 Overview
        sorted_groups = sorted(groups.keys(), key=lambda x: (0 if x == "Overview" else 1, x))
        
        for group_name in sorted_groups:
            content += f"## {group_name}\n"
            # 按文件名排序
            for rel_path, page in sorted(groups[group_name], key=lambda x: x[0]):
                desc = page.description if page.description and page.description != "Docs by LangChain" else ""
                if desc:
                    content += f"- [{page.title}]({rel_path}): {desc}\n"
                else:
                    content += f"- [{page.title}]({rel_path})\n"
            content += "\n"
        
        with open(llms_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n生成索引: {llms_path}")


# ============================================================================
# Mintlify 解析器
# ============================================================================

class MintlifyParser(DocParser):
    """Mintlify 文档站点解析器"""
    
    def fetch_index(self) -> list[DocPage]:
        """从 mint.json 或站点地图获取文档索引"""
        pages = []
        
        # 尝试获取 mint.json
        mint_json_url = urljoin(self.config.base_url, "/mint.json")
        try:
            resp = self.session.get(mint_json_url, timeout=10)
            if resp.status_code == 200:
                mint_config = resp.json()
                pages = self._parse_mint_json(mint_config)
                if pages:
                    return pages
        except Exception:
            pass
        
        # 尝试获取 llms.txt
        llms_txt_url = urljoin(self.config.base_url, "/llms.txt")
        try:
            resp = self.session.get(llms_txt_url, timeout=10)
            if resp.status_code == 200:
                pages = self._parse_llms_txt(resp.text)
                if pages:
                    return pages
        except Exception:
            pass
        
        # 尝试从首页解析导航
        try:
            resp = self.session.get(self.config.base_url, timeout=10)
            if resp.status_code == 200:
                pages = self._parse_navigation(resp.text)
        except Exception as e:
            print(f"警告: 无法获取站点索引 - {e}")
        
        return pages
    
    def _parse_mint_json(self, config: dict) -> list[DocPage]:
        """解析 mint.json 配置"""
        pages = []
        navigation = config.get("navigation", [])
        
        for group in navigation:
            group_name = group.get("group", "")
            for page_path in group.get("pages", []):
                if isinstance(page_path, str):
                    # 简单路径
                    url = urljoin(self.config.base_url, f"/{page_path}")
                    pages.append(DocPage(
                        url=url,
                        title=self._path_to_title(page_path),
                        description=group_name,
                        relative_path=self._url_to_path(url),
                        url_path=urlparse(url).path.strip('/')
                    ))
                elif isinstance(page_path, dict):
                    # 嵌套组
                    for sub_page in page_path.get("pages", []):
                        url = urljoin(self.config.base_url, f"/{sub_page}")
                        pages.append(DocPage(
                            url=url,
                            title=self._path_to_title(sub_page),
                            description=page_path.get("group", group_name),
                            relative_path=self._url_to_path(url),
                            url_path=urlparse(url).path.strip('/')
                        ))
        
        return pages
    
    def _parse_llms_txt(self, content: str) -> list[DocPage]:
        """解析 llms.txt 格式"""
        pages = []
        current_section = ""
        
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("# "):
                current_section = line[2:]
            elif line.startswith("- ["):
                # 解析 markdown 链接: - [Title](url): Description
                match = re.match(r'-\s*\[([^\]]+)\]\(([^)]+)\)(?::\s*(.*))?', line)
                if match:
                    title, url, desc = match.groups()
                    if not url.startswith("http"):
                        url = urljoin(self.config.base_url, url)
                    pages.append(DocPage(
                        url=url,
                        title=title,
                        description=desc or current_section,
                        relative_path=self._url_to_path(url),
                        url_path=urlparse(url).path.strip('/')
                    ))
        
        return pages
    
    def _parse_navigation(self, html: str) -> list[DocPage]:
        """从 HTML 页面解析导航链接"""
        pages = []
        soup = BeautifulSoup(html, 'lxml')
        
        # 查找导航链接
        nav_selectors = [
            'nav a[href]',
            '.sidebar a[href]',
            '[class*="nav"] a[href]',
            '[class*="sidebar"] a[href]',
        ]
        
        seen_urls = set()
        for selector in nav_selectors:
            for link in soup.select(selector):
                href = link.get('href', '')
                if not href or href.startswith('#') or href.startswith('http'):
                    continue
                
                url = urljoin(self.config.base_url, href)
                if url in seen_urls:
                    continue
                seen_urls.add(url)
                
                title = link.get_text(strip=True) or self._path_to_title(href)
                pages.append(DocPage(
                    url=url,
                    title=title,
                    description="",
                    relative_path=self._url_to_path(url),
                    url_path=urlparse(url).path.strip('/')
                ))
        
        return pages
    
    def fetch_content(self, page: DocPage) -> str:
        """获取页面内容并转换为 Markdown"""
        resp = self.session.get(page.url, timeout=30)
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, 'lxml')
        
        # 移除不需要的元素
        for selector in ['script', 'style', 'nav', 'header', 'footer', '.sidebar', '[class*="nav"]']:
            for elem in soup.select(selector):
                elem.decompose()
        
        # 查找主要内容区域
        content_selectors = [
            'article',
            'main',
            '[class*="content"]',
            '[class*="article"]',
            '.prose',
        ]
        
        content = None
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                break
        
        if not content:
            content = soup.body or soup
        
        # 转换为 Markdown
        if html2text:
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.ignore_images = False
            h.body_width = 0  # 不换行
            return h.handle(str(content))
        else:
            return content.get_text(separator='\n\n')
    
    def _path_to_title(self, path: str) -> str:
        """将路径转换为标题"""
        name = Path(path).stem
        return name.replace('-', ' ').replace('_', ' ').title()
    
    def _url_to_path(self, url: str) -> str:
        """将 URL 转换为本地路径，保留层级结构"""
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # 如果配置了 preserve_path，保留完整路径结构
        if getattr(self.config, 'preserve_path', True):
            # 如果配置了 path_prefix，截取相对路径
            prefix = getattr(self.config, 'path_prefix', None)
            if prefix:
                prefix = prefix.strip('/')
                if path.startswith(prefix):
                    path = path[len(prefix):].strip('/')
            
            # 保留路径结构，但清理文件名
            if path:
                # 确保以 .md 结尾
                if not path.endswith('.md'):
                    path += '.md'
                return path
        
        # 回退到旧逻辑：基于关键词判断目录
        if 'guide' in path.lower() or 'tutorial' in path.lower() or 'getting-started' in path.lower():
            prefix = "guides/"
        elif 'api' in path.lower() or 'reference' in path.lower():
            prefix = "references/"
        else:
            prefix = ""
        
        # 清理文件名
        filename = Path(path).name or "index"
        if not filename.endswith('.md'):
            filename += '.md'
        
        return prefix + filename


# ============================================================================
# llms.txt 解析器
# ============================================================================

class LlmsTxtParser(DocParser):
    """llms.txt 标准站点解析器"""
    
    def fetch_index(self) -> list[DocPage]:
        """获取 llms.txt 并解析"""
        resp = self.session.get(self.config.url, timeout=30)
        resp.raise_for_status()
        
        pages = []
        current_section = ""
        base_url = self.config.url.rsplit('/', 1)[0]
        
        for line in resp.text.split("\n"):
            line = line.strip()
            if line.startswith("# "):
                current_section = line[2:]
            elif line.startswith("- ["):
                match = re.match(r'-\s*\[([^\]]+)\]\(([^)]+)\)(?::\s*(.*))?', line)
                if match:
                    title, url, desc = match.groups()
                    if not url.startswith("http"):
                        url = urljoin(base_url + "/", url)
                    
                    # 确定本地路径
                    if "guide" in current_section.lower() or "tutorial" in current_section.lower():
                        rel_path = f"guides/{self._sanitize_filename(title)}.md"
                    elif "reference" in current_section.lower() or "api" in current_section.lower():
                        rel_path = f"references/{self._sanitize_filename(title)}.md"
                    else:
                        rel_path = f"{self._sanitize_filename(title)}.md"
                    
                    pages.append(DocPage(
                        url=url,
                        title=title,
                        description=desc or "",
                        relative_path=rel_path,
                        url_path=urlparse(url).path.strip('/')
                    ))
        
        return pages
    
    def fetch_content(self, page: DocPage) -> str:
        """获取页面内容"""
        resp = self.session.get(page.url, timeout=30)
        resp.raise_for_status()
        
        # 如果是 HTML，转换为 Markdown
        content_type = resp.headers.get('content-type', '')
        if 'html' in content_type:
            soup = BeautifulSoup(resp.text, 'lxml')
            
            # 移除不需要的元素
            for elem in soup.select('script, style, nav, header, footer'):
                elem.decompose()
            
            content = soup.select_one('article, main, .content') or soup.body
            
            if html2text:
                h = html2text.HTML2Text()
                h.body_width = 0
                return h.handle(str(content))
            else:
                return content.get_text(separator='\n\n')
        else:
            return resp.text
    
    def _sanitize_filename(self, name: str) -> str:
        """清理文件名"""
        name = re.sub(r'[^\w\s-]', '', name)
        name = re.sub(r'[-\s]+', '-', name)
        return name.lower().strip('-')


# ============================================================================
# 主程序
# ============================================================================

def load_config(config_path: str = ".docs/sources.yaml") -> list[SourceConfig]:
    """加载配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    sources = []
    for item in data.get("sources", []):
        sources.append(SourceConfig(**item))
    
    return sources


def get_parser(config: SourceConfig, dry_run: bool = False) -> DocParser:
    """根据类型获取解析器"""
    parsers = {
        "mintlify": MintlifyParser,
        "llms-txt": LlmsTxtParser,
    }
    
    parser_class = parsers.get(config.type)
    if not parser_class:
        raise ValueError(f"不支持的站点类型: {config.type}")
    
    return parser_class(config, dry_run)


def main():
    parser = argparse.ArgumentParser(description="同步远程文档到本地")
    parser.add_argument("--source", "-s", help="指定要同步的源名称")
    parser.add_argument("--config", "-c", default=".docs/sources.yaml", help="配置文件路径")
    parser.add_argument("--dry-run", "-n", action="store_true", help="预览模式，不实际下载")
    args = parser.parse_args()
    
    # 加载配置
    try:
        sources = load_config(args.config)
    except FileNotFoundError:
        print(f"错误: 配置文件不存在 - {args.config}")
        sys.exit(1)
    
    if not sources:
        print("警告: 没有配置任何文档源")
        sys.exit(0)
    
    # 过滤源
    if args.source:
        sources = [s for s in sources if s.name == args.source]
        if not sources:
            print(f"错误: 未找到名为 '{args.source}' 的源")
            sys.exit(1)
    
    # 执行同步
    total_pages = 0
    for source in sources:
        try:
            doc_parser = get_parser(source, args.dry_run)
            pages = doc_parser.sync()
            total_pages += len(pages)
        except Exception as e:
            print(f"错误: 同步 {source.name} 失败 - {e}")
    
    print(f"\n{'='*60}")
    print(f"同步完成! 共处理 {total_pages} 个文档页面")


if __name__ == "__main__":
    main()
