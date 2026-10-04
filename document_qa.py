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


print("\nAI DOCUMENT ASSISTANT")
print("=" * 60)
print("Ask questions about the document.")
print("Type 'exit' to stop.")
print("=" * 60)


while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        print("\nAI Document Assistant closed.")
        break

    prompt = f"""
You are an AI document assistant.

Answer the user's question using ONLY the information
available in the document below.

If the answer is not available in the document, say:
"Information not found in the document."

Keep the answer simple and clear.

DOCUMENT:
{full_text}

QUESTION:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:0.5b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    print("\nAI ANSWER")
    print("-" * 50)
    print(result["response"])