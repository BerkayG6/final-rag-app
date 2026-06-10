import fitz

def load_pdf(file_path: str) -> str:
    """Load a PDF file and return its text content."""
    pdf = fitz.open(file_path)
    text = [page.get_text() for page in pdf]
    return "\n".join(text)
