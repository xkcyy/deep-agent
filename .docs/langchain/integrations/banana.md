# Banana

[Banana](https://www.banana.dev/about-us) is focused on building the machine learning infrastructure.

This example goes over how to use LangChain to interact with Banana models

```python  theme={null}
##Installing the langchain packages needed to use the integration
pip install -qU  langchain-community
```

```python  theme={null}
# Install the package  https://docs.banana.dev/banana-docs/core-concepts/sdks/python
pip install -qU  banana-dev
```

```python  theme={null}
# get new tokens: https://app.banana.dev/
# We need three parameters to make a Banana.dev API call:
# * a team api key
# * the model's unique key
# * the model's url slug

import os

# You can get this from the main dashboard
# at https://app.banana.dev
os.environ["BANANA_API_KEY"] = "YOUR_API_KEY"
# OR
# BANANA_API_KEY = getpass()
```

```python  theme={null}
from langchain.chains import LLMChain
from langchain_community.llms import Banana
from langchain_core.prompts import PromptTemplate
```

```python  theme={null}
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)
```

```python  theme={null}
# Both of these are found in your model's
# detail page in https://app.banana.dev
llm = Banana(model_key="YOUR_MODEL_KEY", model_url_slug="YOUR_MODEL_URL_SLUG")
```

```python  theme={null}
llm_chain = LLMChain(prompt=prompt, llm=llm)
```

```python  theme={null}
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/banana.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt