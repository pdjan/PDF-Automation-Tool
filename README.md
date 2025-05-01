# 🛠️ PDF Automation Tool

A command-line PDF utility built with Python for automating common PDF tasks like:
- 📄 Extracting text
- 📚 Merging multiple PDFs
- ✂️ Splitting specific pages
- 🔁 Rotating pages

This tool uses `PyPDF2`, `pdfplumber`, and `tqdm` to provide a clean interface and real-time progress feedback.

---

## 🚀 Features

- ✅ Extract all text from any PDF
- ✅ Merge multiple PDF files into one
- ✅ Split a PDF by selecting a range of pages
- ✅ Rotate a specific page by any angle (90, 180, 270)
- ✅ Live CLI progress bars using `tqdm`

---

## 🧰 Requirements

- Python 3.8+
- Libraries:
  ```bash
  pip install -r requirements.txt

## Usage

python main.py <command> [options]

Extract text
python main.py extract document.pdf

Merge PDFs
python main.py merge file1.pdf file2.pdf -o combined.pdf

Split PDF
python main.py split input.pdf 1 5 -o output.pdf

Rotate page
python main.py rotate input.pdf 1 90 -o rotated.pdf

## Credits
Built with:
- PyPDF2
- pdfplumber
- tqdm

## License
MIT License

