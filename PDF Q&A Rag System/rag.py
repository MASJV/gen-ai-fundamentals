import fitz
import chromadb
import ollama

#STEP 1: Extract PDF Text

pdf = fitz.open("sample.pdf")

text = ""

for page in pdf:
    text += page.get_text()

#STEP 2: Chunking

chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

print("\nChunks Created:")
for chunk in chunks:
    print("-", chunk)

#STEP 3: Create Vector DB

client = chromadb.Client()

collection = client.create_collection(
    name="rag_demo",
    metadata={"hnsw:space": "cosine"}
)

#STEP 4: Store Embeddings

for i, chunk in enumerate(chunks):

    embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=chunk
    )["embedding"]

    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )

print("\nEmbeddings Stored Successfully")

#STEP 5: User Question

question = input("\nAsk a question: ")

#STEP 6: Question Embedding

query_embedding = ollama.embeddings(
    model="nomic-embed-text",
    prompt=question
)["embedding"]

#STEP 7: Similarity Search

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

context = results["documents"][0][0]

print("\nRetrieved Context:")
print(context)

#STEP 8: Simple Relevance Check

question_words = [
    word.lower()
    for word in question.split()
    if len(word) > 3
]

match_count = 0

for word in question_words:
    if word in context.lower():
        match_count += 1

if match_count == 0:
    print("\nAnswer not found in document")

else:

    # -----------------------
    # STEP 9: Generation
    # -----------------------

    prompt = (
        "Answer ONLY using the provided context.\n"
        "If answer is not present in context, "
        "say 'Answer not found in document'.\n\n"
        "Context:\n"
        + context
        + "\n\nQuestion:\n"
        + question
        + "\n\nAnswer:"
    )

    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )

    print("\nAnswer:")
    print(response["response"])