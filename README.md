# 🤖 Local AI Agent

A local AI document assistant built with **Python, LangChain, Ollama, Qwen3, Chroma, and Streamlit**.

The goal of this project is to create a completely local RAG (Retrieval-Augmented Generation) application that can read PDF documents and answer questions about their contents without requiring a paid cloud AI API.

## ✨ Features

* 🧠 Local **Qwen3 14B** language model through Ollama
* 🔎 RAG-based document question answering
* 📄 PDF document support
* 🗃️ Chroma vector database
* 🔢 `nomic-embed-text` for local embeddings
* 💬 Streamlit web chat interface
* 📤 Upload PDF files through the browser
* 🔒 No OpenAI or other paid API key required
* 🖥️ Designed to run locally on your own PC

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │   Streamlit UI  │
                    │     app.py      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     rag.py      │
                    └────────┬────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │  PDF Loader     │     │    Qwen3 14B    │
        │ pdf_loader.py   │     │     Ollama      │
        └────────┬────────┘     └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Text Chunking   │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ nomic-embed-text│
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │     Chroma      │
        │ Vector Database │
        └─────────────────┘
```

## 📁 Project Structure

```text
LocalAIAgent/
│
├── app.py
├── rag.py
├── pdf_loader.py
├── requirements.txt
├── .gitignore
│
└── documents/
    └── .gitkeep
```

### Main files

| File               | Purpose                             |
| ------------------ | ----------------------------------- |
| `app.py`           | Streamlit web interface             |
| `rag.py`           | RAG pipeline and question answering |
| `pdf_loader.py`    | Loads PDF documents                 |
| `requirements.txt` | Python dependencies                 |
| `documents/`       | Local PDF documents                 |

## 💻 Requirements

### Hardware

The application is designed for local AI usage.

Recommended:

* NVIDIA GPU with **12 GB+ VRAM**
* **16 GB+ RAM**
* Windows/Linux
* Python 3.10+

A smaller GPU can be used with a smaller language model.

### Software

Install:

* Python
* Git
* Ollama

Download Ollama from:

https://ollama.com/

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Afran-d/LocalAIAgent.git
cd LocalAIAgent
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell does not allow script execution, you may need to change the execution policy for your user account.

### 3. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install the Ollama models

Pull the language model:

```powershell
ollama pull qwen3:14b
```

Pull the embedding model:

```powershell
ollama pull nomic-embed-text
```

You can verify the installed models with:

```powershell
ollama list
```

You should see both models.

## ▶️ Running the Application

Make sure your virtual environment is activated:

```powershell
.\venv\Scripts\Activate.ps1
```

Start the Streamlit application:

```powershell
python -m streamlit run app.py
```

Streamlit will display a local address similar to:

```text
http://localhost:8501
```

Open that address in your browser.

## 📄 Using a PDF

1. Open the application in your browser.
2. Use the **Upload a PDF** option in the sidebar.
3. Select a PDF file.
4. Ask a question about the document in the chat box.

For example:

```text
What is soybean oil used for?
```

The RAG system retrieves relevant information from the document and provides it to Qwen3.

## 🧪 Testing PDF Loading

You can test the PDF loader separately:

```powershell
python pdf_loader.py
```

It will display information about the pages loaded from the `documents/` directory.

## 🧠 How RAG Works

The application uses Retrieval-Augmented Generation.

```text
PDF
 ↓
Extract text
 ↓
Split into smaller chunks
 ↓
Generate embeddings
 ↓
Store in Chroma
 ↓
User asks a question
 ↓
Search for relevant chunks
 ↓
Relevant context
 ↓
Qwen3 14B
 ↓
Answer
```

This allows the local language model to use information from documents that were not part of its original training data.

## 🌐 Internet Requirements

The application is designed to run locally.

An internet connection is required initially to:

* Install Python packages
* Install Ollama
* Download the AI models
* Clone the GitHub repository

After the required software and models have been downloaded, the AI inference and RAG processing can run locally without sending documents or questions to a cloud AI service.

## ⚠️ Current Limitations

This is an ongoing project.

Current limitations include:

* Scanned/image-only PDFs may not contain extractable text.
* OCR support is not yet implemented.
* The current RAG implementation rebuilds the vector database when processing questions.
* Duplicate document indexing is not yet handled.
* Source/page citations are not yet displayed in the chat.
* Document deletion/management is limited.
* The current interface is a basic prototype.
* The assistant currently uses the retrieved document context as its primary knowledge source.

## 🔨 Planned Improvements

* [ ] Add OCR support for scanned PDFs
* [ ] Improve document indexing
* [ ] Prevent duplicate embeddings
* [ ] Support multiple documents efficiently
* [ ] Add source and page citations
* [ ] Add document management
* [ ] Add chat history controls
* [ ] Improve Streamlit UI
* [ ] Add hybrid RAG + general knowledge mode
* [ ] Improve error handling
* [ ] Add more local AI models
* [ ] Improve multilingual support

## 🎯 Motivation

This project was created to learn how modern local AI systems work by building one from the ground up.

The project focuses on understanding:

* Local Large Language Models
* Ollama
* LangChain
* Retrieval-Augmented Generation
* Vector databases
* Embeddings
* PDF processing
* AI application development
* Local/offline AI architectures

The long-term goal is to develop a capable local AI assistant without depending on paid cloud AI APIs.

## 🛠️ Technology Stack

* **Python**
* **LangChain**
* **Ollama**
* **Qwen3 14B**
* **nomic-embed-text**
* **ChromaDB**
* **Streamlit**
* **PyPDF**
* **Git / GitHub**

## 📜 License

This project is currently intended as a personal learning and development project.
