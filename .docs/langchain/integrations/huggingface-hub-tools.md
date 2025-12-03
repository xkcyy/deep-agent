# HuggingFace Hub Tools

> [Huggingface Tools](https://huggingface.co/docs/transformers/v4.29.0/en/custom_tools) that supporting text I/O can be
> loaded directly using the `load_huggingface_tool` function.

```python  theme={null}
# Requires transformers>=4.29.0 and huggingface_hub>=0.14.1
pip install -qU  transformers huggingface_hub > /dev/null
```

```python  theme={null}
pip install -qU  langchain-community
```

```python  theme={null}
from langchain_community.agent_toolkits.load_tools import load_huggingface_tool

tool = load_huggingface_tool("lysandre/hf-model-downloads")

print(f"{tool.name}: {tool.description}")
```

```output  theme={null}
model_download_counter: This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub. It takes the name of the category (such as text-classification, depth-estimation, etc), and returns the name of the checkpoint
```

```python  theme={null}
tool.run("text-classification")
```

```output  theme={null}
'facebook/bart-large-mnli'
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/huggingface_tools.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt