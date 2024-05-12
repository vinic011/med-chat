from langchain_community.document_loaders import PyMuPDFLoader

def load_pdf_pages(file_path):
    loader = PyMuPDFLoader(file_path)
    pages = loader.load()
    return pages

def load_pdf_text(file_path):
    loader = PyMuPDFLoader(file_path)
    pages = loader.load()
    raw_text = "\n\n".join([page.page_content for page in pages])
    return raw_text
    