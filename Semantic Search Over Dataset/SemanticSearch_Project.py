import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os


df = pd.read_csv("products.csv")   # columns: id, title, description, category
docs = (df["title"] + " " + df["description"]).tolist()


model = SentenceTransformer("BAAI/bge-small-en-v1.5") 

if os.path.exists("doc_embeddings.npy"):
    doc_vecs = np.load("doc_embeddings.npy")
else:
    doc_vecs = model.encode(
        docs,
        batch_size=64,
        show_progress_bar=True
    )
    np.save("doc_embeddings.npy", doc_vecs)

def search(query, category="laptop", top_k=5):

    # Metadata filter
    filtered_df = df[df["category"] == category]

    # Use only filtered embeddings
    filtered_vecs = doc_vecs[filtered_df.index]

    q_vec = model.encode(
        "Represent this for retrieval: " + query 
    )

    scores = cosine_similarity([q_vec], filtered_vecs)[0]

    top_idx = np.argsort(scores)[::-1][:top_k]

    results = filtered_df.iloc[top_idx][["title"]].copy()
    results["score"] = scores[top_idx].round(3)

    return results.reset_index(drop=True)


print(search("lightweight laptop for programming", top_k=3))
print(search("heavyweight laptop for programming", top_k=3)) 