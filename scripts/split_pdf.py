"""Split a PDF into smaller chunks for processing."""

import argparse
import os
from pypdf import PdfReader, PdfWriter


def split_pdf(input_path: str, output_dir: str, chunk_size: int = 15) -> None:
    """Split a PDF into chunks of specified page size.

    Args:
        input_path: Path to the input PDF file
        output_dir: Directory to save the chunks
        chunk_size: Number of pages per chunk (default: 15)
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Read the PDF
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")

    # Split into chunks
    chunk_num = 1
    for start in range(0, total_pages, chunk_size):
        end = min(start + chunk_size, total_pages)
        writer = PdfWriter()

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        # Get base name from input file
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(
            output_dir,
            f"{base_name}_chunk{chunk_num:02d}_pages{start+1}-{end}.pdf"
        )

        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"Created: chunk{chunk_num:02d} (pages {start+1}-{end})")
        chunk_num += 1

    print(f"\nDone! Created {chunk_num-1} chunks in {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a PDF into smaller chunks")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_dir", help="Directory to save the chunks")
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=15,
        help="Number of pages per chunk (default: 15)"
    )

    args = parser.parse_args()
    split_pdf(args.input_pdf, args.output_dir, args.chunk_size)
