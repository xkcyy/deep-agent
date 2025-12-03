# MLX

> [MLX](https://ml-explore.github.io/mlx/build/html/index.html) is a `NumPy`-like array framework
> designed for efficient and flexible machine learning on `Apple` silicon,
> brought to you by `Apple machine learning research`.

## Installation and Setup

Install several Python packages:

<CodeGroup>
  ```bash pip theme={null}
  pip install mlx-lm transformers huggingface_hub
  ```

  ```bash uv theme={null}
  uv add mlx-lm transformers huggingface_hub
  ```
</CodeGroup>

## Chat models

See a [usage example](/oss/python/integrations/chat/mlx).

```python  theme={null}
from langchain_community.chat_models.mlx import ChatMLX
```

## LLMs

### MLX Local Pipelines

See a [usage example](/oss/python/integrations/llms/mlx_pipelines).

```python  theme={null}
from langchain_community.llms.mlx_pipeline import MLXPipeline
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/mlx.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt