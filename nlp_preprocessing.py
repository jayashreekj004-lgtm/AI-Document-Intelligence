import re
from pypdf import PdfReader
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")

pdf_path = "documents/COMPANY EMPLOYEE POLICY DOCUMENT.pdf"

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()
    full_text += text + " "


# Convert text to lowercase
text = full_text.lower()

# Remove extra spaces
text = re.sub(r"\s+", " ", text)

# Remove special characters
text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

# Split text into words
words = text.split()

# Remove stopwords
stop_words = set(stopwords.words("english"))

filtered_words = []

for word in words:
    if word not in stop_words:
        filtered_words.append(word)


print("Original word count:", len(words))
print("After stopword removal:", len(filtered_words))

print("\nFirst 50 important words:")
print(filtered_words[:50])