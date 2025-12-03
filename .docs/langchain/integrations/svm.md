# SVM

> [Support vector machines (SVMs)](https://scikit-learn.org/stable/modules/svm.html#support-vector-machines) are a set of supervised learning methods used for classification, regression and outliers detection.

This notebook goes over how to use a retriever that under the hood uses an `SVM` using `scikit-learn` package.

Largely based on [github.com/karpathy/randomfun/blob/master/knn\_vs\_svm.html](https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.html)

```python  theme={null}
pip install -qU  scikit-learn
```

```python  theme={null}
pip install -qU  lark
```

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

```python  theme={null}
import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")
```

```output  theme={null}
OpenAI API Key: ········
```

```python  theme={null}
from langchain_community.retrievers import SVMRetriever
from langchain_openai import OpenAIEmbeddings
```

## Create New Retriever with Texts

```python  theme={null}
retriever = SVMRetriever.from_texts(
    ["foo", "bar", "world", "hello", "foo bar"], OpenAIEmbeddings()
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

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/retrievers/svm.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt