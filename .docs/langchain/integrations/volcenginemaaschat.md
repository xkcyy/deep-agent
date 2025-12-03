# VolcEngineMaasChat

This guide provides you with a guide on how to get started with volc engine maas chat models.

```python  theme={null}
# Install the package
pip install -qU  volcengine
```

```python  theme={null}
from langchain_community.chat_models import VolcEngineMaasChat
from langchain.messages import HumanMessage
```

```python  theme={null}
chat = VolcEngineMaasChat(volc_engine_maas_ak="your ak", volc_engine_maas_sk="your sk")
```

or you can set access\_key and secret\_key in your environment variables

```bash  theme={null}
export VOLC_ACCESSKEY=YOUR_AK
export VOLC_SECRETKEY=YOUR_SK
```

```python  theme={null}
chat([HumanMessage(content="给我讲个笑话")])
```

```output  theme={null}
AIMessage(content='好的，这是一个笑话：\n\n为什么鸟儿不会玩电脑游戏？\n\n因为它们没有翅膀！')
```

# volc engine maas chat with stream

```python  theme={null}
chat = VolcEngineMaasChat(
    volc_engine_maas_ak="your ak",
    volc_engine_maas_sk="your sk",
    streaming=True,
)
```

```python  theme={null}
chat([HumanMessage(content="给我讲个笑话")])
```

```output  theme={null}
AIMessage(content='好的，这是一个笑话：\n\n三岁的女儿说她会造句了，妈妈让她用“年轻”造句，女儿说：“妈妈减肥，一年轻了好几斤”。')
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat/volcengine_maas.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt