import requests
from pypdf import PdfReader

# PDF path
pdf_path = "documents/COMPANY EMPLOYEE POLICY DOCUMENT.pdf"

# Read PDF
reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()
    full_text += text + "\n"

# Create prompt for LLM
prompt = f"""
You are an AI document assistant.

Read the following employee policy document and create a simple summary.

Give the summary in:
1. Main purpose of the document
2. Important employee policies
3. Leave policy
4. Attendance policy
5. Working hours
6. Important rules

Use simple English and short bullet points.

DOCUMENT:
{full_text}
"""

# Send document to Ollama
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:0.5b",
        "prompt": prompt,
        "stream": False
    }
)

# Get AI response
result = response.json()

print("\nAI DOCUMENT SUMMARY")
print("=" * 60)
print(result["response"])