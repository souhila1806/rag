import documents
from pathlib import Path
import frontmatter

def ingest_documents(path):
    dir = Path(path)
    docs = []

    for file in dir.glob("*.md"):
        post = frontmatter.load(file)
        docs.append({"metadata": post.metadata, "content": post.content})

    return docs