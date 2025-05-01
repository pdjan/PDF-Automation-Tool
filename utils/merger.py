from PyPDF2 import PdfMerger
from tqdm import tqdm

def merge_pdfs_with_progress(pdf_list, output):
    merger = PdfMerger()
    for pdf in tqdm(pdf_list, desc="Merging PDFs", unit="file"):
        merger.append(pdf)
    merger.write(output)
    merger.close()
