from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="qwen3:14b")

template = """
You are a helpful assistant. Answer the following question as best you can. 


You have access to the following tools:
here some relevant informations:{context}
here is the questions to anser:{question}


"""


prompt = ChatPromptTemplate.from_template(template)
chain =  prompt | model

while True:
    print("\n============================================================\n\n")
    print("Welcome to the Qwen3:14b chatbot! Type 'q' to exit.\n")
    
    question = input("Enter your question(q to exit): ")
    if question =="q":
        break
    context = retriever.invoke(question)    
    result = chain.invoke({"context": context, "question": question})
    print(result)

