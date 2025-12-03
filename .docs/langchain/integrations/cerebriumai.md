# CerebriumAI

`Cerebrium` is an AWS Sagemaker alternative. It also provides API access to [several LLM models](https://docs.cerebrium.ai/cerebrium/prebuilt-models/deployment).

This notebook goes over how to use LangChain with [CerebriumAI](https://docs.cerebrium.ai/introduction).

## Install cerebrium

The `cerebrium` package is required to use the `CerebriumAI` API. Install `cerebrium` using `pip3 install cerebrium`.

```python  theme={null}
# Install the package
!pip3 install cerebrium
```

## Imports

```python  theme={null}
import os

from langchain.chains import LLMChain
from langchain_community.llms import CerebriumAI
from langchain_core.prompts import PromptTemplate
```

## Set the Environment API Key

Make sure to get your API key from CerebriumAI. See [here](https://dashboard.cerebrium.ai/login). You are given a 1 hour free of serverless GPU compute to test different models.

```python  theme={null}
os.environ["CEREBRIUMAI_API_KEY"] = "YOUR_KEY_HERE"
```

## Create the CerebriumAI instance

You can specify different parameters such as the model endpoint url, max length, temperature, etc. You must provide an endpoint url.

```python  theme={null}
llm = CerebriumAI(endpoint_url="YOUR ENDPOINT URL HERE")
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
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/cerebriumai.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt