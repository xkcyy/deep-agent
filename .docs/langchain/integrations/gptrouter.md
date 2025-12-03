# GPTRouter

[GPTRouter](https://github.com/Writesonic/GPTRouter) is an open source LLM API Gateway that offers a universal API for 30+ LLMs, vision, and image models, with smart fallbacks based on uptime and latency, automatic retries, and streaming.

This notebook covers how to get started with using LangChain + the GPTRouter I/O library.

* Set `GPT_ROUTER_API_KEY` environment variable
* or use the `gpt_router_api_key` keyword argument

```python  theme={null}
pip install -qU  GPTRouter
```

```python  theme={null}
from langchain_community.chat_models import GPTRouter
from langchain_community.chat_models.gpt_router import GPTRouterModel
from langchain.messages import HumanMessage
```

```python  theme={null}
anthropic_claude = GPTRouterModel(name="claude-instant-1.2", provider_name="anthropic")
```

```python  theme={null}
chat = GPTRouter(models_priority_list=[anthropic_claude])
```

```python  theme={null}
messages = [
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    )
]
chat(messages)
```

```output  theme={null}
AIMessage(content=" J'aime programmer.")
```

## `GPTRouter` also supports async and streaming functionality

```python  theme={null}
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
```

```python  theme={null}
await chat.agenerate([messages])
```

```output  theme={null}
LLMResult(generations=[[ChatGeneration(text=" J'aime programmer.", generation_info={'finish_reason': 'stop_sequence'}, message=AIMessage(content=" J'aime programmer."))]], llm_output={}, run=[RunInfo(run_id=UUID('9885f27f-c35a-4434-9f37-c254259762a5'))])
```

```python  theme={null}
chat = GPTRouter(
    models_priority_list=[anthropic_claude],
    streaming=True,
    verbose=True,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)
chat(messages)
```

```output  theme={null}
 J'aime programmer.
```

```output  theme={null}
AIMessage(content=" J'aime programmer.")
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat/gpt_router.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt