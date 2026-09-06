from index import calculate_question_embedding
from langchain_ollama import ChatOllama
from prompts import PROMPT
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from eval_set import eval_set
from utils import build_context

def evaluate(index, chunked_documents):
    hit=0
    miss=0
    for item in eval_set:
        question = item["question"]
        expected_answer = item["expected_answer"]
        expected_source = item["expected_source"]

        question_embedding = calculate_question_embedding(question)
        distances, indices = index.search(question_embedding, k=3)
        if expected_source is not None:
            if expected_source in [chunked_documents[i]["metadata"].get("source", "unknown") for i in indices[0]]:
                hit += 1
                print(f"Question: {question}\nExpected Answer: {expected_answer}\nExpected Source: {expected_source}\n Result: Hit\n")
            else:
                miss += 1
                print(f"Question: {question}\nExpected Answer: {expected_answer}\nExpected Source: {expected_source}\n Result: Miss\n")
    print(f"Total hits:rate {hit/(hit+miss)}")
    print(f"Total misses:rate {miss/(hit+miss)}")


def evaluate_refusal(index, chunked_documents):

    #The chatbot
    llm = ChatOllama(model="llama3.2")
    prompt_template = PromptTemplate(template=PROMPT, input_variables=["question", "context"])
    chain= prompt_template | llm | StrOutputParser()
    none_questions = [item for item in eval_set if item["expected_source"] is None]
    for item in none_questions:
        question = item["question"]

        question_embedding = calculate_question_embedding(question)
        distances, indices = index.search(question_embedding, k=3)
        context = build_context(chunked_documents, indices)
        #generate the answer using the chain
        answer = chain.invoke({"question": question, "context": context})
        print(f"Question: {question}\n Generated Answer: {answer}\n")

