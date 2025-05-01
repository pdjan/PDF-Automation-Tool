from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

def split_pdf(file_path, start, end, output_path):
    reader = PdfReader(file_path)
    writer = PdfWriter()

    total_pages = end - start
    for i in tqdm(range(start, end), desc="Splitting pages", unit="page"):
        writer.add_page(reader.pages[i])

    with open(output_path, "wb") as f:
        writer.write(f)
