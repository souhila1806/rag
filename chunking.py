from langchain_text_splitters import SpacyTextSplitter

def chunk_text(text):
    splitter = SpacyTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_text(text)
    return chunks


def chunk_documents(documents):
    chunked_docs = []
    for doc in documents:
        content = doc["content"]
        metadata = doc["metadata"]
        chunks = chunk_text(content)
        for i, chunk in enumerate(chunks):
            chunked_docs.append({"metadata": metadata, "content": chunk, "chunk_index": i})
    return chunked_docs