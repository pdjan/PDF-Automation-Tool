import pdfplumber
from tqdm import tqdm

def extract_text_with_progress(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in tqdm(pdf.pages, desc="Extracting text", unit="page"):
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text
