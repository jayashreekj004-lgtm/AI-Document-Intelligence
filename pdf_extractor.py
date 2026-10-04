from pypdf import PdfReader
pdf_path = "documents/COMPANY EMPLOYEE POLICY DOCUMENT.pdf"

reader = PdfReader(pdf_path)

print("Number of pages:", len(reader.pages))

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()

    print("\n" + "=" * 50)
    print("PAGE", page_number)
    print("=" * 50)

    print(text)
    