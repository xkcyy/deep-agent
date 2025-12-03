# Git

> [Git](https://en.wikipedia.org/wiki/Git) is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers collaboratively developing source code during software development.

This notebook shows how to load text files from `Git` repository.

## Load existing repository from disk

```python  theme={null}
pip install -qU  GitPython
```

```python  theme={null}
from git import Repo

repo = Repo.clone_from(
    "https://github.com/langchain-ai/langchain", to_path="./example_data/test_repo1"
)
branch = repo.head.reference
```

```python  theme={null}
from langchain_community.document_loaders import GitLoader
```

```python  theme={null}
loader = GitLoader(repo_path="./example_data/test_repo1/", branch=branch)
```

```python  theme={null}
data = loader.load()
```

```python  theme={null}
len(data)
```

```python  theme={null}
print(data[0])
```

```output  theme={null}
page_content='.venv\n.github\n.git\n.mypy_cache\n.pytest_cache\nDockerfile' metadata={'file_path': '.dockerignore', 'file_name': '.dockerignore', 'file_type': ''}
```

## Clone repository from url

```python  theme={null}
from langchain_community.document_loaders import GitLoader
```

```python  theme={null}
loader = GitLoader(
    clone_url="https://github.com/langchain-ai/langchain",
    repo_path="./example_data/test_repo2/",
    branch="master",
)
```

```python  theme={null}
data = loader.load()
```

```python  theme={null}
len(data)
```

```output  theme={null}
1074
```

## Filtering files to load

```python  theme={null}
from langchain_community.document_loaders import GitLoader

# e.g. loading only python files
loader = GitLoader(
    repo_path="./example_data/test_repo1/",
    file_filter=lambda file_path: file_path.endswith(".py"),
)
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/git.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt