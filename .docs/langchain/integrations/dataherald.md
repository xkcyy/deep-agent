# Dataherald

This notebook goes over how to use the dataherald component.

First, you need to set up your Dataherald account and get your API KEY:

1. Go to dataherald and sign up [here](https://www.dataherald.com/)
2. Once you are logged in your Admin Console, create an API KEY
3. pip install dataherald

Then we will need to set some environment variables:

1. Save your API KEY into DATAHERALD\_API\_KEY env variable

```python  theme={null}
pip install dataherald
pip install -qU langchain-community
```

```python  theme={null}
import os

os.environ["DATAHERALD_API_KEY"] = ""
```

```python  theme={null}
from langchain_community.utilities.dataherald import DataheraldAPIWrapper
```

```python  theme={null}
dataherald = DataheraldAPIWrapper(db_connection_id="65fb766367dd22c99ce1a12d")
```

```python  theme={null}
dataherald.run("How many employees are in the company?")
```

```output  theme={null}
'select COUNT(*) from employees'
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/dataherald.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt