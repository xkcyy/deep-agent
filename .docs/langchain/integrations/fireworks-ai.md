# Fireworks AI

> [Fireworks AI](https://fireworks.ai) is a generative AI inference platform to run and
> customize models with industry-leading speed and production-readiness.

## Installation and setup

* Install the Fireworks integration package.

  ```bash  theme={null}
  pip install langchain-fireworks
  ```

* Get a Fireworks API key by signing up at [fireworks.ai](https://fireworks.ai).

* Authenticate by setting the FIREWORKS\_API\_KEY environment variable.

### Authentication

There are two ways to authenticate using your Fireworks API key:

1. Setting the `FIREWORKS_API_KEY` environment variable.

   ```python  theme={null}
   os.environ["FIREWORKS_API_KEY"] = "<KEY>"
   ```

2. Setting `api_key` field in the Fireworks LLM module.

   ```python  theme={null}
   llm = Fireworks(api_key="<KEY>")
   ```

## Chat models

See a [usage example](/oss/python/integrations/chat/fireworks).

```python  theme={null}
from langchain_fireworks import ChatFireworks
```

## LLMs

See a [usage example](/oss/python/integrations/llms/fireworks).

```python  theme={null}
from langchain_fireworks import Fireworks
```

## Embedding models

See a [usage example](/oss/python/integrations/text_embedding/fireworks).

```python  theme={null}
from langchain_fireworks import FireworksEmbeddings
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/fireworks.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt