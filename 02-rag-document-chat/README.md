<div align="center">

# 📄 RAG Document Q&A — Chat With Your Documents

A command-line tool that lets you ask questions about any text or PDF document and get accurate, grounded answers — powered by Retrieval-Augmented Generation (RAG) using Google's Gemini API and ChromaDB.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Gemini_API-4285F4?style=flat&logo=google&logoColor=white)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)

</div>

---

## 📖 Overview

This project is the second build in my [AI Engineering Journey](../README.md) — moving from simple API integration ([Project 01](../01-weather-cli)) into **Retrieval-Augmented Generation (RAG)**, one of the most in-demand patterns in real-world AI engineering today.

Instead of relying purely on an LLM's training knowledge, this tool lets you feed it **your own document** — a PDF or text file — and ask questions that get answered using content actually retrieved from that file. If the answer isn't in the document, the model says so instead of guessing.

**Example interaction:**
```
RAG Document Q&A Tool
========================================
Enter path to your document (.txt or .pdf): documents/food.txt
Loading document...
Chunking document...
Created 4 chunks.
Embedding and storing chunks...
Document ready. Ask your questions below.

Ask a question: What ingredients are mentioned?

💬 The document mentions tomatoes, garlic, olive oil, and basil 
   as the main ingredients for the recipe described.
```

---

## ✨ Features

- 📂 **Multi-format support** — works with both `.txt` and `.pdf` documents
- ✂️ **Smart chunking** — splits documents with overlap to preserve context across boundaries
- 🧠 **Semantic search** — retrieves the most relevant sections using vector embeddings, not just keyword matching
- 🤖 **Grounded AI answers** — Gemini generates responses strictly from retrieved context, reducing hallucination
- 🗄️ **Local vector storage** — uses ChromaDB, no external database or paid service required
- 🛡️ **Robust error handling** — graceful handling of missing files, bad API keys, and embedding failures

---

## 🛠️ Tech Stack

| Component          | Technology                     | Purpose                                  |
|---------------------|--------------------------------|-------------------------------------------|
| Language             | Python 3.10+                    | Core implementation                        |
| Document Parsing     | `pypdf`                          | Extracts text from PDF files               |
| Embeddings           | Gemini (`gemini-embedding-001`) | Converts text into semantic vectors        |
| Vector Database      | ChromaDB                         | Stores and searches embeddings locally     |
| Answer Generation    | Gemini (`gemini-2.0-flash`)      | Generates natural-language answers         |
| Config Management    | `python-dotenv`                  | Secure API key handling                    |

---

## 🧩 How It Works (RAG Pipeline)

```
Document → Chunking → Embedding → Vector Store
                                        │
User Question → Embedding → Similarity Search
                                        │
                              Top Matching Chunks
                                        │
                         Chunks + Question → Gemini
                                        │
                              Grounded Answer
```

1. **Load** — the document is read and its raw text extracted
2. **Chunk** — text is split into overlapping segments to preserve context
3. **Embed** — each chunk is converted into a numerical vector representing its meaning
4. **Store** — vectors are saved in a local ChromaDB collection
5. **Retrieve** — when a question is asked, it's embedded too, and the most similar chunks are fetched
6. **Generate** — Gemini answers the question using only the retrieved chunks as context

---

## 📁 Project Structure

```
02-rag-document-chat/
├── src/
│   ├── loader.py         # Reads .txt / .pdf files
│   ├── chunker.py        # Splits text into overlapping chunks
│   ├── embedder.py       # Generates embeddings via Gemini
│   ├── vector_store.py   # Stores & searches embeddings (ChromaDB)
│   ├── qa.py             # Combines retrieval + generation
│   └── main.py           # CLI entry point
├── documents/             # Sample documents for testing
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- A free [Google Gemini API key](https://aistudio.google.com/apikey)

### Installation

```bash
# Clone the repository
git clone https://github.com/Muhammad-Abdullah01/ai-engineering-journey.git
cd ai-engineering-journey/02-rag-document-chat

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root (use `.env.example` as a reference):

```env
GEMINI_API_KEY=your_gemini_key_here
```

### Run it

```bash
cd src
python main.py
```

Enter the path to a `.txt` or `.pdf` file when prompted, then ask questions about its content. Type `quit` to exit.

---

## 🧠 What I Learned Building This

- Core RAG concepts: chunking, embeddings, semantic search, and grounded generation
- Working with a local vector database (ChromaDB) instead of relying on external paid services
- Writing prompts that constrain an LLM to answer only from provided context, reducing hallucination
- Debugging real-world issues: outdated model names (`text-embedding-004` → `gemini-embedding-001`), API parameter typos, and virtual environment corruption
- The difference between a "bloated" `requirements.txt` (unrelated packages from a different environment) and a "large but correct" one (legitimate dependencies of the libraries actually used)
- Managing Python virtual environments more resiliently, including fallback tooling (`virtualenv`) when built-in `venv` misbehaves

---

## 🗺️ Roadmap / Ideas for Improvement

- [ ] Support multiple documents in a single session
- [ ] Add a persistent vector store so documents don't need re-embedding every run
- [ ] Show source chunks alongside each answer for transparency
- [ ] Build a simple web interface using Streamlit
- [ ] Add automated tests for chunking and retrieval accuracy

---

<div align="center">

## 👤 Author

**Muhammad Abdullah**

Part of my [AI Engineering Journey](../README.md) — documenting my transition from a BS Data Science graduate into AI Engineering, one project at a time.

</div>

---

<div align="center">

## 📄 License

This project is open source and available under the [MIT License](../LICENSE).

</div>
