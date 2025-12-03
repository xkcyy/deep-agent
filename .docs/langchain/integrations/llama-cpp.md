# Llama.cpp

> [llama.cpp python](https://github.com/abetlen/llama-cpp-python) library is a simple Python bindings for `@ggerganov`
> [llama.cpp](https://github.com/ggerganov/llama.cpp).
>
> This package provides:
>
> * Low-level access to C API via ctypes interface.
> * High-level Python API for text completion
>   * `OpenAI`-like API
>   * `LangChain` compatibility
>   * `LlamaIndex` compatibility
> * OpenAI compatible web server
>   * Local Copilot replacement
>   * Function Calling support
>   * Vision API support
>   * Multiple Models

```python  theme={null}
pip install -qU  llama-cpp-python
```

```python  theme={null}
from langchain_community.embeddings import LlamaCppEmbeddings
```

```python  theme={null}
llama = LlamaCppEmbeddings(model_path="/path/to/model/ggml-model-q4_0.bin")
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = llama.embed_query(text)
```

```python  theme={null}
doc_result = llama.embed_documents([text])
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/llamacpp.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt