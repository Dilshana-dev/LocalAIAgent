from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader


DOCUMENTS_DIR = "documents"


def load_pdfs():
    """
    Load all PDF files from the documents directory.
    """

    documents_path = Path(DOCUMENTS_DIR)

    if not documents_path.exists():
        print(f"Documents directory not found: {DOCUMENTS_DIR}")
        return []

    loader = PyPDFDirectoryLoader(DOCUMENTS_DIR)

    documents = loader.load()

    print(f"Loaded {len(documents)} PDF pages.")

    return documents


if __name__ == "__main__":
    documents = load_pdfs()

    for document in documents[:3]:
        print("\n--- Document ---")
        print("Source:", document.metadata.get("source"))
        print("Page:", document.metadata.get("page"))
        print("Content:")
        print(document.page_content[:500])