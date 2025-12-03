# TF-IDF

> [TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting) means term-frequency times inverse document-frequency.

This notebook goes over how to use a retriever that under the hood uses [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) using `scikit-learn` package.

For more information on the details of TF-IDF see [this blog post](https://medium.com/data-science-bootcamp/tf-idf-basics-of-information-retrieval-48de122b2a4c).

```python  theme={null}
pip install -qU  scikit-learn
```

```python  theme={null}
from langchain_community.retrievers import TFIDFRetriever
```

## Create New Retriever with Texts

```python  theme={null}
retriever = TFIDFRetriever.from_texts(["foo", "bar", "world", "hello", "foo bar"])
```

## Create a New Retriever with Documents

You can now create a new retriever with the documents you created.

```python  theme={null}
from langchain_core.documents import Document

retriever = TFIDFRetriever.from_documents(
    [
        Document(page_content="foo"),
        Document(page_content="bar"),
        Document(page_content="world"),
        Document(page_content="hello"),
        Document(page_content="foo bar"),
    ]
)
```

## Use Retriever

We can now use the retriever!

```python  theme={null}
result = retriever.invoke("foo")
```

```python  theme={null}
result
```

```output  theme={null}
[Document(page_content='foo', metadata={}),
 Document(page_content='foo bar', metadata={}),
 Document(page_content='hello', metadata={}),
 Document(page_content='world', metadata={})]
```

## Save and load

You can easily save and load this retriever, making it handy for local development!

```python  theme={null}
retriever.save_local("testing.pkl")
```

```python  theme={null}
retriever_copy = TFIDFRetriever.load_local("testing.pkl")
```

```python  theme={null}
retriever_copy.invoke("foo")
```

```output  theme={null}
[Document(page_content='foo', metadata={}),
 Document(page_content='foo bar', metadata={}),
 Document(page_content='hello', metadata={}),
 Document(page_content='world', metadata={})]
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/retrievers/tf_idf.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt