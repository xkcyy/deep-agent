# SparkLLM

[SparkLLM](https://xinghuo.xfyun.cn/spark) is a large-scale cognitive model independently developed by iFLYTEK.
It has cross-domain knowledge and language understanding ability by learning a large amount of texts, codes and images.
It can understand and perform tasks based on natural dialogue.

## Prerequisite

* Get SparkLLM's app\_id, api\_key and api\_secret from [iFlyTek SparkLLM API Console](https://console.xfyun.cn/services/bm3) (for more info, see [iFlyTek SparkLLM Intro](https://xinghuo.xfyun.cn/sparkapi) ), then set environment variables `IFLYTEK_SPARK_APP_ID`, `IFLYTEK_SPARK_API_KEY` and `IFLYTEK_SPARK_API_SECRET` or pass parameters when creating `ChatSparkLLM` as the demo above.

## Use SparkLLM

```python  theme={null}
import os

os.environ["IFLYTEK_SPARK_APP_ID"] = "app_id"
os.environ["IFLYTEK_SPARK_API_KEY"] = "api_key"
os.environ["IFLYTEK_SPARK_API_SECRET"] = "api_secret"
```

```python  theme={null}
from langchain_community.llms import SparkLLM

# Load the model
llm = SparkLLM()

res = llm.invoke("What's your name?")
print(res)
```

```output  theme={null}
/Users/liugddx/code/langchain/libs/core/langchain_core/_api/deprecation.py:117: LangChainDeprecationWarning: The function `__call__` was deprecated in LangChain 0.1.7 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(
```

```output  theme={null}
My name is iFLYTEK Spark. How can I assist you today?
```

```python  theme={null}
res = llm.generate(prompts=["hello!"])
res
```

```output  theme={null}
LLMResult(generations=[[Generation(text='Hello! How can I assist you today?')]], llm_output=None, run=[RunInfo(run_id=UUID('d8cdcd41-a698-4cbf-a28d-e74f9cd2037b'))])
```

```python  theme={null}
for res in llm.stream("foo:"):
    print(res)
```

```output  theme={null}
Hello! How can I assist you today?
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/sparkllm.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt