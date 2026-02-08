from langchain_community.document_loaders import PyPDFLoader

def load_documents():
    pra_loader = PyPDFLoader("data/pra_rulebook.pdf")
    corep_loader = PyPDFLoader("data/corep_instructions.pdf")

    pra_docs = pra_loader.load()
    corep_docs = corep_loader.load()

    return pra_docs + corep_docs
