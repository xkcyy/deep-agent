# Wolfram Alpha

This notebook goes over how to use the wolfram alpha component.

First, you need to set up your Wolfram Alpha developer account and get your APP ID:

1. Go to wolfram alpha and sign up for a developer account [here](https://developer.wolframalpha.com/)
2. Create an app and get your APP ID
3. pip install wolframalpha

Then we will need to set some environment variables:

1. Save your APP ID into WOLFRAM\_ALPHA\_APPID env variable

```python  theme={null}
pip install wolframalpha
```

```python  theme={null}
import os

os.environ["WOLFRAM_ALPHA_APPID"] = ""
```

```python  theme={null}
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
```

```python  theme={null}
wolfram = WolframAlphaAPIWrapper()
```

```python  theme={null}
wolfram.run("What is 2x+5 = -3x + 7?")
```

```output  theme={null}
'x = 2/5'
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/wolfram_alpha.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt