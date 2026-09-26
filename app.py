import streamlit as st
from pathlib import Path

from rag import ask_question


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Local AI Agent",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🤖 Local AI Agent")

st.write(
    "Ask questions about your local PDF documents "
    "using Qwen3 and RAG."
)


# -----------------------------
# PDF upload
# -----------------------------

st.sidebar.header("📄 Documents")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    documents_dir = Path("documents")
    documents_dir.mkdir(exist_ok=True)

    file_path = documents_dir / uploaded_file.name

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.sidebar.success(
        f"Uploaded: {uploaded_file.name}"
    )


# -----------------------------
# Chat history
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat input
# -----------------------------

question = st.chat_input(
    "Ask something about your documents..."
)


if question:

    # Display user's question

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)


    # Generate answer

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                answer = ask_question(question)

                st.markdown(answer)

            except Exception as e:

                answer = f"Error: {e}"

                st.error(answer)


    # Save assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )