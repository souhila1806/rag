from ingest import ingest_documents
from chunking import chunk_documents
from index import create_index
from evaluate import evaluate, evaluate_refusal
from retreive_generate import chat_rag
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["chat", "eval", "eval-refusal"])
    args = parser.parse_args()


    path = "./documents"
    #read documents from the specified path
    documents = ingest_documents(path)

    #chunk the documents into smaller pieces
    chunked_documents = chunk_documents(documents)
    print(f"Chunked {len(chunked_documents)} documents.")

    index = create_index(chunked_documents)

    if args.mode == "chat":
        chat_rag(chunked_documents, index)
    elif args.mode == "eval":
        evaluate(index, chunked_documents)
    elif args.mode == "eval-refusal":
        evaluate_refusal(index, chunked_documents)

