# Baichuan LLM

Baichuan Inc. ([www.baichuan-ai.com/](https://www.baichuan-ai.com/)) is a Chinese startup in the era of AGI, dedicated to addressing fundamental human needs: Efficiency, Health, and Happiness.

```python  theme={null}
##Installing the langchain packages needed to use the integration
pip install -qU langchain-community
```

## Prerequisite

An API key is required to access Baichuan LLM API. Visit [platform.baichuan-ai.com/](https://platform.baichuan-ai.com/) to get your API key.

## Use Baichuan LLM

```python  theme={null}
import os

os.environ["BAICHUAN_API_KEY"] = "YOUR_API_KEY"
```

```python  theme={null}
from langchain_community.llms import BaichuanLLM

# Load the model
llm = BaichuanLLM()

res = llm.invoke("What's your name?")
print(res)
```

```python  theme={null}
res = llm.generate(prompts=["你好！"])
res
```

```python  theme={null}
for res in llm.stream("Who won the second world war?"):
    print(res)
```

```python  theme={null}
import asyncio


async def run_aio_stream():
    async for res in llm.astream("Write a poem about the sun."):
        print(res)


asyncio.run(run_aio_stream())
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/baichuan.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt