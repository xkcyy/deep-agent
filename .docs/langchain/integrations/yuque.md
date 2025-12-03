# Yuque

> [Yuque](https://www.yuque.com/) is a professional cloud-based knowledge base for team collaboration in documentation.

This notebook covers how to load documents from `Yuque`.

You can obtain the personal access token by clicking on your personal avatar in the [Personal Settings](https://www.yuque.com/settings/tokens) page.

```python  theme={null}
from langchain_community.document_loaders import YuqueLoader
```

```python  theme={null}
loader = YuqueLoader(access_token="<your_personal_access_token>")
```

```python  theme={null}
docs = loader.load()
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/yuque.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt