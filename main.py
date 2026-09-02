from ingest import ingest_documents
from chunking import chunk_documents
from index import create_index, calculate_question_embedding
from langchain_ollama import ChatOllama
from prompts import PROMPT
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



if __name__ == "__main__":
    path = "./documents"
    #read documents from the specified path
    documents = ingest_documents(path)

    #chunk the documents into smaller pieces
    chunked_documents = chunk_documents(documents)
    print(f"Chunked {len(chunked_documents)} documents.")

    index = create_index(chunked_documents)

    #The chatbot
    llm = ChatOllama(model="llama3.2")
    prompt_template = PromptTemplate(template=PROMPT, input_variables=["question", "context"])
    chain= prompt_template | llm | StrOutputParser()

    stop= False
    print("Enter your question (or type 'exit' to quit): ")
    while not stop:
        question = input("User: ")
        if question.lower() == "exit":
            stop = True
            continue

        
        question_embedding = calculate_question_embedding(question)
        #find the 2 most similar chunks to the question
        distances, indices = index.search(question_embedding,k=2)
        context = "\n".join([chunked_documents[i]["content"] for i in indices[0]])
        #generate the answer using the chain
        answer = chain.invoke({"question": question, "context": context})
        print(f"Most relevant chunk: \n chunk {indices[0]}{chunked_documents[indices[0][0]]['metadata']}\n")
        print(f"Second most relevant chunk: \n chunk {indices[0]}{chunked_documents[indices[0][1]]['metadata']}\n")
        print(f"Agent: {answer}")

