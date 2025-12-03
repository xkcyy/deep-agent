# Twitter (via Apify)

This notebook shows how to load chat messages from Twitter to fine-tune on. We do this by utilizing Apify.

First, use Apify to export tweets. An example

```python  theme={null}
import json

from langchain_community.adapters.openai import convert_message_to_dict
from langchain.messages import AIMessage
```

```python  theme={null}
with open("example_data/dataset_twitter-scraper_2023-08-23_22-13-19-740.json") as f:
    data = json.load(f)
```

```python  theme={null}
# Filter out tweets that reference other tweets, because it's a bit weird
tweets = [d["full_text"] for d in data if "t.co" not in d["full_text"]]
# Create them as AI messages
messages = [AIMessage(content=t) for t in tweets]
# Add in a system message at the start
# TODO: we could try to extract the subject from the tweets, and put that in the system message.
system_message = {"role": "system", "content": "write a tweet"}
data = [[system_message, convert_message_to_dict(m)] for m in messages]
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat_loaders/twitter.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt