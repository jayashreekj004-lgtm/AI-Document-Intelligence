import re
from pypdf import PdfReader

pdf_path = "documents/COMPANY EMPLOYEE POLICY DOCUMENT.pdf"

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()
    full_text += text + "\n"


# Remove extra spaces
cleaned_text = re.sub(r"\s+", " ", full_text)

# Remove leading and trailing spaces
cleaned_text = cleaned_text.strip()


print("CLEANED TEXT")
print("=" * 60)
print(cleaned_text)