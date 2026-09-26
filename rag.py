from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from pdf_loader import load_pdfs


# -----------------------------
# Configuration
# -----------------------------

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "qwen3:14b"
CHROMA_DIR = "chroma_langchain_db"


# -----------------------------
# Create embeddings
# -----------------------------

embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)


# -----------------------------
# Load and split documents
# -----------------------------

def create_chunks():
    documents = load_pdfs()

    if not documents:
        print("No PDF documents found.")
        return []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} text chunks.")

    return chunks


# -----------------------------
# Create / load Chroma database
# -----------------------------

def create_vector_database():
    chunks = create_chunks()

    if not chunks:
        return None

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    print("Vector database created successfully.")

    return vector_store


# -----------------------------
# Create the RAG retriever
# -----------------------------

def create_retriever():
    vector_store = create_vector_database()

    if vector_store is None:
        return None

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    return retriever


# -----------------------------
# Ask the local AI
# -----------------------------

def ask_question(question):
    retriever = create_retriever()

    if retriever is None:
        return "No documents are available."

    relevant_documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in relevant_documents
    )

    prompt = f"""
You are a helpful local AI assistant.

Answer the user's question using the provided context.

If the answer cannot be found in the context,  answer  using your own knowledge and say that the information
is not available in the provided documents.

Context:
{context}

Question:
{question}

Answer:
"""

    llm = OllamaLLM(model=LLM_MODEL)

    answer = llm.invoke(prompt)

    return answer


# -----------------------------
# Test the RAG system
# -----------------------------

if __name__ == "__main__":

    question = input("Ask a question: ")

    answer = ask_question(question)

    print("\nAI:")
    print(answer)