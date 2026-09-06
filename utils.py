def build_context(chunked_documents, indices):
    context_parts = []
    for rank, i in enumerate(indices[0], start=1):
        source = chunked_documents[i]["metadata"].get("source", "unknown")
        chunk_id = f"[{rank}] {source}"
        context_parts.append(f"{chunk_id}\n{chunked_documents[i]['content']}")
    return "\n\n".join(context_parts)