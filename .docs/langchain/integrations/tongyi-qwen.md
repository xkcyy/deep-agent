# Tongyi Qwen

Tongyi Qwen is a large-scale language model developed by Alibaba's Damo Academy. It is capable of understanding user intent through natural language understanding and semantic analysis, based on user input in natural language. It provides services and assistance to users in different domains and tasks. By providing clear and detailed instructions, you can obtain results that better align with your expectations.

## Setting up

```python  theme={null}
# Install the package
pip install -qU  langchain-community dashscope
```

```python  theme={null}
# Get a new token: https://help.aliyun.com/document_detail/611472.html?spm=a2c4g.2399481.0.0
from getpass import getpass

DASHSCOPE_API_KEY = getpass()
```

```output  theme={null}
 ········
```

```python  theme={null}
import os

os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY
```

```python  theme={null}
from langchain_community.llms import Tongyi
```

```python  theme={null}
Tongyi().invoke("What NFL team won the Super Bowl in the year Justin Bieber was born?")
```

```output  theme={null}
'Justin Bieber was born on March 1, 1994. The Super Bowl that took place in the same year was Super Bowl XXVIII, which was played on January 30, 1994. The winner of that Super Bowl was the Dallas Cowboys, who defeated the Buffalo Bills with a score of 30-13.'
```

## Using in a chain

```python  theme={null}
from langchain_core.prompts import PromptTemplate
```

```python  theme={null}
llm = Tongyi()
```

```python  theme={null}
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)
```

```python  theme={null}
chain = prompt | llm
```

```python  theme={null}
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

chain.invoke({"question": question})
```

```output  theme={null}
'Justin Bieber was born on March 1, 1994. The Super Bowl that took place in the same calendar year was Super Bowl XXVIII, which was played on January 30, 1994. The winner of Super Bowl XXVIII was the Dallas Cowboys, who defeated the Buffalo Bills with a score of 30-13.'
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/tongyi.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt