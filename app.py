import streamlit as st
import requests
from pypdf import PdfReader


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("📄 AI Document Intelligence System")

st.write(
    "Upload a PDF document and interact with it using AI."
)

st.divider()


# ============================================================
# UPLOAD DOCUMENT
# ============================================================

st.header("📁 Upload Document")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
    key="pdf_uploader"
)


# ============================================================
# PROCESS PDF
# ============================================================

if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    st.write("File name:", uploaded_file.name)

    # --------------------------------------------------------
    # READ PDF
    # --------------------------------------------------------

    reader = PdfReader(uploaded_file)

    full_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            full_text += text + "\n"


    if not full_text.strip():

        st.error("Could not extract text from this PDF.")

        st.stop()


    # --------------------------------------------------------
    # CREATE PAGE-BASED CHUNKS
    # --------------------------------------------------------

    chunks = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            chunks.append(page_text)


    st.info(
        f"Document divided into {len(chunks)} chunks."
    )


    # --------------------------------------------------------
    # VIEW EXTRACTED TEXT
    # --------------------------------------------------------

    with st.expander("📄 View Extracted Text"):

        st.text_area(
            "Document Content",
            full_text,
            height=300,
            key="document_content"
        )


    st.divider()


    # ========================================================
    # AI SUMMARY
    # ========================================================

    st.header("🤖 AI Document Summary")

    if st.button(
        "Generate AI Summary",
        key="summary_button"
    ):

        summary_prompt = f"""
You are an AI document assistant.

Read the following employee policy document.

Create a simple and accurate summary.

Include:

1. Main purpose of the document
2. Working hours
3. Leave policy
4. Attendance policy
5. Employee responsibilities
6. Information security rules
7. Important workplace rules

Use ONLY information available in the document.

Do not invent information.

DOCUMENT:
{full_text}
"""

        try:

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "qwen2.5:0.5b",
                    "prompt": summary_prompt,
                    "stream": False
                },
                timeout=120
            )

            result = response.json()

            if "response" in result:

                st.success("AI Summary")

                st.write(result["response"])

            else:

                st.error(
                    "AI model did not return a response."
                )

        except Exception as e:

            st.error(
                f"An error occurred: {e}"
            )


    st.divider()


    # ========================================================
    # QUESTION ANSWERING
    # ========================================================

    st.header("💬 Ask Questions About Your Document")

    question = st.text_input(
        "Enter your question",
        key="user_question"
    )


    if st.button(
        "Ask AI",
        key="ask_ai_button"
    ):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            # ------------------------------------------------
            # SECTION KEYWORDS
            # ------------------------------------------------

            section_keywords = {

                "responsibilities": [
                    "responsibilities",
                    "assigned tasks",
                    "company policies",
                    "professional behavior",
                    "manager"
                ],

                "security": [
                    "security",
                    "protect company information",
                    "confidential information",
                    "password",
                    "sensitive information",
                    "authorized",
                    "security incidents"
                ],

                "leave": [
                    "leave",
                    "vacation",
                    "sick leave",
                    "personal leave",
                    "annual leave"
                ],

                "working": [
                    "working hours",
                    "work hours",
                    "office hours"
                ],

                "attendance": [
                    "attendance",
                    "absence",
                    "late",
                    "punctuality"
                ]
            }


            # ------------------------------------------------
            # FIND MATCHING KEYWORDS
            # ------------------------------------------------

            question_lower = question.lower()

            matched_keywords = []

            for section, keywords in section_keywords.items():

                for keyword in keywords:

                    if keyword in question_lower:

                        matched_keywords.append(keyword)


            # ------------------------------------------------
            # SCORE DOCUMENT CHUNKS
            # ------------------------------------------------

            scored_chunks = []

            for chunk in chunks:

                chunk_lower = chunk.lower()

                score = 0


                # Question words
                question_words = question_lower.split()

                for word in question_words:

                    if len(word) > 2 and word in chunk_lower:

                        score += 1


                # Section keywords
                for keyword in matched_keywords:

                    if keyword in chunk_lower:

                        score += 5


                if score > 0:

                    scored_chunks.append(
                        (score, chunk)
                    )


            # ------------------------------------------------
            # SORT BY SCORE
            # ------------------------------------------------

            scored_chunks.sort(
                key=lambda x: x[0],
                reverse=True
            )


            # ------------------------------------------------
            # SELECT RELEVANT CHUNKS
            # ------------------------------------------------

            if scored_chunks:

                relevant_chunks = []

                for score, chunk in scored_chunks[:3]:

                    relevant_chunks.append(chunk)

                best_chunk = "\n\n".join(
                    relevant_chunks
                )

            else:

                best_chunk = ""


            # ------------------------------------------------
            # ASK AI
            # ------------------------------------------------

            if not best_chunk:

                st.warning(
                    "Information not found in the document."
                )

            else:

                prompt = f"""
You are an AI document assistant.

Answer the user's question using ONLY the
document content provided below.

Rules:

- Do not invent information.
- Do not guess.
- Do not use outside knowledge.
- If the answer is not available in the document,
  say exactly:

Information not found in the document.

Give a short and clear answer.

DOCUMENT CONTENT:
{best_chunk}

QUESTION:
{question}
"""


                try:

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


                    if "response" in result:

                        st.success("AI Answer")

                        st.write(
                            result["response"]
                        )

                    else:

                        st.error(
                            "AI model did not return a response."
                        )


                except requests.exceptions.ConnectionError:

                    st.error(
                        "Could not connect to Ollama. "
                        "Please make sure Ollama is running."
                    )


                except Exception as e:

                    st.error(
                        f"An error occurred: {e}"
                    )


else:

    st.info(
        "Please upload a PDF document to start."
    )