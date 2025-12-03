# ReadTheDocs Documentation

> [Read the Docs](https://readthedocs.org/) is an open-sourced free software documentation hosting platform. It generates documentation written with the `Sphinx` documentation generator.

This notebook covers how to load content from HTML that was generated as part of a `Read-The-Docs` build.

For an example of this in the wild, see [here](https://github.com/langchain-ai/chat-langchain).

This assumes that the HTML has already been scraped into a folder. This can be done by uncommenting and running the following command

```python  theme={null}
pip install -qU  beautifulsoup4
```

```python  theme={null}
#!wget -r -A.html -P rtdocs https://python.langchain.com/en/latest/
```

```python  theme={null}
from langchain_community.document_loaders import ReadTheDocsLoader
```

```python  theme={null}
loader = ReadTheDocsLoader("rtdocs")
```

```python  theme={null}
docs = loader.load()
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/readthedocs_documentation.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt