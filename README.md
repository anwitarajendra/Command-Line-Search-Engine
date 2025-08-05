# Command Line Search Engine 

A simple yet powerful offline search engine built in Python. It indexes a folder of plain text files and lets you search through them instantly using keyword queries. Perfect for fast document lookup, LLM notes retrieval, and offline NLP-based search experiments.

## Features

-  Full-text search over .txt files
-  Inverted Index for fast lookup
-  Contextual snippets from matching lines
-  Command Line + Optional Streamlit UI
-  No internet required (fully offline)

## Tech Stack

- Python 3
- os, re, collections (for indexing)
- Streamlit (for optional web interface)

## 🧪 How It Works

1. The script reads all .txt files inside the docs/ folder.
2. An inverted index is built mapping each word to the documents and line numbers it appears in.
3. The user enters a search query (single word or multiple keywords).
4. It returns matching file names and lines containing the terms.

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/mini-search-engine.git
   cd mini-search-engine
   ```

2. Add your .txt files into the docs/ folder.

3. To run the command-line version:
   ```bash
   python search.py
   ```

4. To use the Streamlit UI (optional):
   ```bash
   pip install streamlit
   streamlit run app.py
   ```

## Example Use Case

Search for AI terms like:
```
> Enter your search query: transformer
```
Returns:
```
 Found in: llm_fundamentals.txt
  - Line 4: Transformer architecture revolutionized NLP.
```

## Notes

- All files must be in plain .txt format inside the docs/ directory.
- No internet or external API required — works offline.
- Ideal for personal note search, educational summaries, and ML paper references.


Student | Cloud + Python Enthusiast  
JSS Science and Technology University  
