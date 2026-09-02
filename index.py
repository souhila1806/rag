import faiss
from sentence_transformers import SentenceTransformer

def calculate_question_embedding(question):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode([question], convert_to_numpy=True)

def calculate_embeddings(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    return model.encode([chunk["content"] for chunk in chunks], convert_to_numpy=True)

def create_index(chunks):
    embeddings = calculate_embeddings(chunks)
    print(f"embeddings shape: {embeddings.shape}")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print(f"Index created with {index.ntotal} vectors.")
    return index