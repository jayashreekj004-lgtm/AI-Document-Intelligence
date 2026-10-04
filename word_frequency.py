import re
from collections import Counter
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


# Convert to lowercase
text = full_text.lower()

# Remove special characters
text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

# Split into words
words = text.split()

# Remove stopwords
stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words
    if word not in stop_words
]

# Count word frequency
word_counts = Counter(filtered_words)

# Get top 20 words
top_words = word_counts.most_common(20)

print("\nTOP 20 MOST FREQUENT WORDS")
print("=" * 40)

for word, count in top_words:
    print(f"{word}: {count}")
    