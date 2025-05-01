import argparse
from tqdm import tqdm
from utils.extractor import extract_text_with_progress
from utils.merger import merge_pdfs_with_progress
from utils.splitter import split_pdf
from utils.rotator import rotate_pdf

def main():
    parser = argparse.ArgumentParser(description="PDF Automation Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Extract text
    extract_parser = subparsers.add_parser("extract", help="Extract text from a PDF")
    extract_parser.add_argument("file", help="Path to the PDF file")

    # Merge PDFs
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDF files")
    merge_parser.add_argument("files", nargs='+', help="List of PDF files to merge")
    merge_parser.add_argument("-o", "--output", default="merged_output.pdf", help="Output file name")

    # Split PDF
    split_parser = subparsers.add_parser("split", help="Split a PDF file")
    split_parser.add_argument("file", help="PDF file to split")
    split_parser.add_argument("start", type=int, help="Start page (0-indexed)")
    split_parser.add_argument("end", type=int, help="End page (non-inclusive)")
    split_parser.add_argument("-o", "--output", default="split_output.pdf", help="Output file name")

    # Rotate page
    rotate_parser = subparsers.add_parser("rotate", help="Rotate a page in a PDF")
    rotate_parser.add_argument("file", help="PDF file")
    rotate_parser.add_argument("page", type=int, help="Page number to rotate (0-indexed)")
    rotate_parser.add_argument("angle", type=int, help="Rotation angle (90, 180, 270)")
    rotate_parser.add_argument("-o", "--output", default="rotated_output.pdf", help="Output file name")

    args = parser.parse_args()

    # Command handling
    if args.command == "extract":
        text = extract_text_with_progress(args.file)
        print("\n\n--- Extracted Text ---\n")
        print(text)

    elif args.command == "merge":
        merge_pdfs_with_progress(args.files, args.output)
        print(f"\nMerged files saved as '{args.output}'")

    elif args.command == "split":
        split_pdf(args.file, args.start, args.end, args.output)
        print(f"Split pages saved as '{args.output}'")

    elif args.command == "rotate":
        rotate_pdf(args.file, args.page, args.angle, args.output)
        print(f"Rotated PDF saved as '{args.output}'")

if __name__ == "__main__":
    main()
