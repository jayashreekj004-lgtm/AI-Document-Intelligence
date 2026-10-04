import re
from pypdf import PdfReader

pdf_path = "documents/COMPANY EMPLOYEE POLICY DOCUMENT.pdf"

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()
    full_text += text + "\n"


# Find numbered section headings
pattern = r"\b\d+\.\s+[A-Z][A-Z\s&]+\b"

topics = re.findall(pattern, full_text)

print("\nDOCUMENT TOPICS")
print("=" * 40)

for topic in topics:
    print(topic.strip())