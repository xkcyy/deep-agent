# iFlytek

> [iFlytek](https://www.iflytek.com) is a Chinese information technology company
> established in 1999. It creates voice recognition software and
> voice-based internet/mobile products covering education, communication,
> music, intelligent toys industries.

## Installation and Setup

* Get `SparkLLM` app\_id, api\_key and api\_secret from [iFlyTek SparkLLM API Console](https://console.xfyun.cn/services/bm3) (for more info, see [iFlyTek SparkLLM Intro](https://xinghuo.xfyun.cn/sparkapi)).
* Install the Python package (not for the embedding models):

<CodeGroup>
  ```bash pip theme={null}
  pip install websocket-client
  ```

  ```bash uv theme={null}
  uv add websocket-client
  ```
</CodeGroup>

## LLMs

See a [usage example](/oss/python/integrations/llms/sparkllm).

```python  theme={null}
from langchain_community.llms import SparkLLM
```

## Chat models

See a [usage example](/oss/python/integrations/chat/sparkllm).

```python  theme={null}
from langchain_community.chat_models import ChatSparkLLM
```

## Embedding models

```python  theme={null}
from langchain_community.embeddings import SparkLLMTextEmbeddings
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/iflytek.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt