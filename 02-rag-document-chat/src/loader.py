from pathlib import Path
from pypdf import PdfReader

class DocumentLoadError(Exception):
    pass

def load_documnet(file_path: str) -> str:
    """
    Load text content from a .txt or .pdf file.
    """

    path = Path(file_path)

    if not path.exists():
        raise DocumentLoadError(f"File not found: {file_path}")
    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")
    elif path.suffix.lower():
        try:
            reader = PdfReader(str(path))
            text =""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            raise DocumentLoadError(f"Could not read PDF: {e}")
    else:
        raise DocumentLoadError(f"Unsupported file type: {path.suffix}")

