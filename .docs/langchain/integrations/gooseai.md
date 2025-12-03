# GooseAI

`GooseAI` is a fully managed NLP-as-a-Service, delivered via API. GooseAI provides access to [these models](https://goose.ai/docs/models).

This notebook goes over how to use LangChain with [GooseAI](https://goose.ai/).

## Install openai

The `openai` package is required to use the GooseAI API. Install `openai` using `pip install openai`.

```python  theme={null}
pip install -qU  langchain-openai
```

## Imports

```python  theme={null}
import os

from langchain.chains import LLMChain
from langchain_community.llms import GooseAI
from langchain_core.prompts import PromptTemplate
```

## Set the Environment API Key

Make sure to get your API key from GooseAI. You are given \$10 in free credits to test different models.

```python  theme={null}
from getpass import getpass

GOOSEAI_API_KEY = getpass()
```

```python  theme={null}
os.environ["GOOSEAI_API_KEY"] = GOOSEAI_API_KEY
```

## Create the GooseAI instance

You can specify different parameters such as the model name, max tokens generated, temperature, etc.

```python  theme={null}
llm = GooseAI()
```

## Create a Prompt Template

We will create a prompt template for Question and Answer.

```python  theme={null}
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)
```

## Initiate the LLMChain

```python  theme={null}
llm_chain = LLMChain(prompt=prompt, llm=llm)
```

## Run the LLMChain

Provide a question and run the LLMChain.

```python  theme={null}
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/gooseai.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt