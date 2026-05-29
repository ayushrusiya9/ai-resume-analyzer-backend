import fitz # PyMuPDF

def extract_text_from_pdf(pdf_bytes_or_path):
    """Extract text from a PDF file given as bytes or file path"""
    if isinstance(pdf_bytes_or_path, (bytes, bytearray)):
        doc = fitz.open(stream=pdf_bytes_or_path, filetype="pdf")
    else:
        doc = fitz.open(pdf_bytes_or_path)
    pages = [page.get_text() for page in doc]
    doc.close()
    return "\n".join(pages)