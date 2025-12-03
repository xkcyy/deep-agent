# AI/ML API

> [AI/ML API](https://aimlapi.com/app/?utm_source=langchain\&utm_medium=github\&utm_campaign=integration) provides a single API for accessing 300+ hosted foundation models (DeepSeek, Gemini, GPT, and more) with enterprise-grade uptime and throughput.

## Installation and setup

* Install the AI/ML API integration package.

  ```bash  theme={null}
  pip install langchain-aimlapi
  ```

* Create an account at [aimlapi.com](https://aimlapi.com/app/?utm_source=langchain\&utm_medium=github\&utm_campaign=integration) and generate an API key.

* Authenticate by setting the `AIMLAPI_API_KEY` environment variable.

```python  theme={null}
import os

os.environ["AIMLAPI_API_KEY"] = "aimlapi_..."
```

## Chat models

See a [usage example](/oss/python/integrations/chat/aimlapi).

```python  theme={null}
from langchain_aimlapi import ChatAimlapi
```

## LLMs

See a [usage example](/oss/python/integrations/llms/aimlapi).

```python  theme={null}
from langchain_aimlapi import AimlapiLLM
```

## Embedding models

See a [usage example](/oss/python/integrations/text_embedding/aimlapi).

```python  theme={null}
from langchain_aimlapi import AimlapiEmbeddings
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/aimlapi.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt