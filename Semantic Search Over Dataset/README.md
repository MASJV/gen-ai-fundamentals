# Semantic Search over a Custom Dataset

A meaning-based product search engine that searches a custom CSV dataset using
sentence embeddings instead of exact keyword matching. Product titles and
descriptions are converted into vectors, cached locally, and compared against
a natural-language query using cosine similarity, with an optional category
filter to keep results relevant.

## Architecture

```text
products.csv (id, title, description, category)
      |
Combine title + description per product
      |
SentenceTransformer (BAAI/bge-small-en-v1.5)
      |
Check for cached embeddings
      |
doc_embeddings.npy
(load if available / generate and save if missing)
      |
User Query + Category Filter
      |
Query Embedding
      |
Cosine Similarity
      |
Top-K Most Similar Products
```

## Files

| File                        | Role                                                                                                        |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `SemanticSearch_Project.py` | Everything — dataset loading, embedding generation, caching, category filtering, similarity search, ranking |
| `products.csv`              | Custom dataset containing `id`, `title`, `description`, and `category`                                      |
| `doc_embeddings.npy`        | Cached product embeddings generated on the first run and reused on later runs                               |

## Setup

1. Install dependencies:

   ```bash
   pip install pandas numpy sentence-transformers scikit-learn
   ```

2. Make sure `products.csv` is in the same folder as the script with these
   columns:

   ```text
   id, title, description, category
   ```

3. Run it:

   ```bash
   python SemanticSearch_Project.py
   ```

4. Edit the `search()` calls at the bottom of the script to try different
   queries, categories, and `top_k` values, e.g.

   ```python
   search("lightweight laptop for programming", category="laptop", top_k=3)
   ```

## How it works, in plain words

1. **Prepare the dataset** — The script loads `products.csv` and combines each
   product's title and description into one searchable text document.

2. **Embed and cache** — `BAAI/bge-small-en-v1.5` converts every product into
   a numerical embedding. If `doc_embeddings.npy` already exists, the script
   loads those saved embeddings instead of generating them again.

3. **Filter by category** — Before similarity comparison, products are filtered
   by the requested category, such as `"laptop"`, so only relevant items are
   considered.

4. **Embed the query** — The natural-language search query is converted into an
   embedding using the same Sentence Transformer model.

5. **Compare and rank** — Cosine similarity measures how close the query
   embedding is to each filtered product embedding. The highest-scoring
   products are returned as the Top-K results.

This means a query such as *"lightweight laptop for programming"* can retrieve
products with semantically similar descriptions even when they do not contain
the exact same words — meaning-based search rather than simple keyword
matching.

> **Note:** If `products.csv` is changed, delete `doc_embeddings.npy` before
> running the script again so fresh embeddings are generated for the updated
> dataset.

## Cost notes

Runs locally using `sentence-transformers` — **zero API cost**. After the
embedding model has been downloaded, searches and embedding generation can run
locally on the available CPU or GPU.
