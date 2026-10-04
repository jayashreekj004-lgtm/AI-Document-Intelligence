# AI Document Intelligence System

An AI-powered document analysis system that allows users to upload PDF documents, generate summaries, and ask questions about the document using NLP, RAG, and a local LLM.

## Features

- PDF document upload
- PDF text extraction
- Text cleaning and NLP preprocessing
- Word frequency analysis
- Topic extraction
- AI-generated document summary
- Question answering from the document
- Basic RAG-based document retrieval
- Information-not-found handling
- Streamlit web interface
- Local LLM integration using Ollama

## Technologies Used

- Python
- Streamlit
- PyPDF
- NLTK
- Scikit-learn
- Requests
- Ollama
- Qwen 2.5 0.5B
- NLP
- RAG
- LLM

## Project Structure

```text
AI-Document-Intelligence/
│
├── data/
│
├── documents/
│   └── COMPANY EMPLOYEE POLICY DOCUMENT.pdf
│
├── app.py
├── pdf_extractor.py
├── text_cleaner.py
├── nlp_preprocessing.py
├── word_frequency.py
├── topic_extractor.py
├── summarizer.py
├── document_qa.py
├── document_rag.py
├── requirements.txt
└── README.md
How It Works
User uploads a PDF document.
The system extracts text from the PDF.
NLP techniques are used to preprocess and analyze the text.
The document is divided into smaller chunks.
Relevant chunks are retrieved based on the user's question.
The retrieved information is sent to the local LLM.
The LLM generates an answer using the document content.
The system can also generate an AI summary of the document.
AI Model

This project uses:

Qwen 2.5 0.5B

The model runs locally through Ollama.

Running the Project
Step 1: Install dependencies


pip install -r requirements.txt

Step 2:

ollama run qwen2.5:0.5b
Keep Ollama running while using the application

Step 3:
Open another terminal in the project folder and run:
streamlit run app.py


Step 4:
Open the Streamlit URL shown in the terminal.
Example:
http://localhost:8501

Example Questions

Users can ask questions such as:

What are the working hours?
What is the leave policy?
What are the employee responsibilities?
How should employees protect company information?
What is the company salary?

If the requested information is not available in the document, the system responds accordingly.

Example Output

Question:

What are the working hours?

Answer:

The standard working hours of TechNova Solutions are 9:00 AM to 6:00 PM.

Future Improvements
Better semantic search using embeddings
Vector database integration
Multi-document support
Chat history
Improved RAG retrieval
Document comparison
Support for DOCX and TXT files
More advanced LLM models
Project Status

Completed basic AI Document Intelligence System with:

NLP
LLM
RAG
PDF processing
Streamlit interface

