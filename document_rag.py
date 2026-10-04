import requests
from pypdf import PdfReader

# 1. Read PDF
pdf_path = "documents/COMPANY EMPLOYEE POLICY DOCUMENT.pdf"

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()
    full_text += text + "\n"


# 2. Split PDF into chunks
chunk_size = 500
chunks = []

for i in range(0, len(full_text), chunk_size):
    chunks.append(full_text[i:i + chunk_size])

print("Total chunks:", len(chunks))


# 3. Ask a question
question = input("\nAsk a question: ").lower()


# 4. Find the relevant chunk
question_words = question.split()

best_chunk = ""
best_score = 0

for chunk in chunks:
    score = 0
    chunk_lower = chunk.lower()

    for word in question_words:
        if word in chunk_lower:
            score += 1

    if score > best_score:
        best_score = score
        best_chunk = chunk


# 5. Check whether a relevant chunk was found
if not best_chunk or best_score == 0:
    print("Information not found in the document.")

else:
    # 6. Send relevant chunk to the AI model
    prompt = f"""
    Answer the question using only the document content below.

    If the answer is not available, say:
    Information not found in the document.

    DOCUMENT CONTENT:
    {best_chunk}

    QUESTION:
    {question}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:0.5b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    result = response.json()

    print("\nAI RAG ANSWER")
    print("=" * 50)
    print(result["response"])