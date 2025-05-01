from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

def rotate_pdf(file_path, page_number, angle, output_path):
    reader = PdfReader(file_path)
    writer = PdfWriter()

    for i, page in enumerate(tqdm(reader.pages, desc="Rotating PDF", unit="page")):
        if i == page_number:
            page.rotate(angle)  # or page.rotate_clockwise(angle)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
