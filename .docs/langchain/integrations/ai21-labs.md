# AI21 Labs

> [AI21 Labs](https://www.ai21.com/about) is a company specializing in Natural
> Language Processing (NLP), which develops AI systems
> that can understand and generate natural language.

This page covers how to use the `AI21` ecosystem within `LangChain`.

## Installation and Setup

* Get an AI21 api key and set it as an environment variable (`AI21_API_KEY`)
* Install the Python package:

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-ai21
  ```

  ```bash uv theme={null}
  uv add langchain-ai21
  ```
</CodeGroup>

## Chat models

### AI21 Chat

See a [usage example](/oss/python/integrations/chat/ai21).

```python  theme={null}
from langchain_ai21 import ChatAI21
```

## Deprecated features

:::caution The following features are deprecated.
:::

### AI21 LLM

```python  theme={null}
from langchain_ai21 import AI21LLM
```

### AI21 Contextual Answer

```python  theme={null}
from langchain_ai21 import AI21ContextualAnswers
```

## Text splitters

### AI21 Semantic Text Splitter

```python  theme={null}
from langchain_ai21 import AI21SemanticTextSplitter
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/ai21.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt