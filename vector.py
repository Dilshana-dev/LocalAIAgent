from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


df = pd.read_csv("content01.csv")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for index, row in df.iterrows():
        content = row["content"] + " " + row["Review"]
        metadata = {"source": row['source'], "title": row['title'], "date": row['date'], "url": row['url']}
        document = Document(page_content=content, metadata=metadata, id=str(index))
        
        
    ids.append(str(index))
    documents.append(document)


    db = Chroma.from_documents(documents, embeddings, persist_directory=db_location)
    

vectorstore = Chroma(
    collection_name="content01",
    persist_directory=db_location, 
    embedding_function=embeddings

    )

if add_documents:
    vectorstore.add_documents(documents, ids=ids)



retriever = vectorstore.as_retriever(
    search_kwargs={"k": 7})

