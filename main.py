import argparse, json
from pathlib import Path
from pypdf import PdfReader
from pdf_outline import flatten_outline, to_markdown

def main():
    parser=argparse.ArgumentParser(description="Export a PDF bookmark outline.")
    parser.add_argument("pdf",type=Path)
    parser.add_argument("--format",choices=("markdown","json"),default="markdown")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    try:
        reader=PdfReader(str(args.pdf))
        items=flatten_outline(reader.outline,reader.get_destination_page_number)
    except Exception as exc:
        parser.error(f"could not read PDF outline: {exc}")
    output=to_markdown(items,args.pdf.stem) if args.format=="markdown" else json.dumps(items,indent=2)
    if args.output: args.output.write_text(output+"\n",encoding="utf-8")
    else: print(output)
    return 0

if __name__=="__main__": raise SystemExit(main())
