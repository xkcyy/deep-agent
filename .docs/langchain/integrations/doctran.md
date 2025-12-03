# Doctran

> [Doctran](https://github.com/psychic-api/doctran) is a python package. It uses LLMs and open-source
> NLP libraries to transform raw text into clean, structured, information-dense documents
> that are optimized for vector space retrieval. You can think of `Doctran` as a black box where
> messy strings go in and nice, clean, labelled strings come out.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install doctran
  ```

  ```bash uv theme={null}
  uv add doctran
  ```
</CodeGroup>

## Document Transformers

### Document Interrogator

See a [usage example for DoctranQATransformer](/oss/python/integrations/document_transformers/doctran_interrogate_document).

```python  theme={null}
from langchain_community.document_transformers import DoctranQATransformer
```

### Property Extractor

See a [usage example for DoctranPropertyExtractor](/oss/python/integrations/document_transformers/doctran_extract_properties).

```python  theme={null}
from langchain_community.document_transformers import DoctranPropertyExtractor
```

### Document Translator

See a [usage example for DoctranTextTranslator](/oss/python/integrations/document_transformers/doctran_translate_document).

```python  theme={null}
from langchain_community.document_transformers import DoctranTextTranslator
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/doctran.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt