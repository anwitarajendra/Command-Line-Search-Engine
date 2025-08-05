import streamlit as st
import os
import re
import math
from collections import defaultdict
import pandas as pd

# --- Phase 1: Inverted Index Construction ---
def build_inverted_index(folder_path):
    inverted_index = defaultdict(list)
    doc_lengths = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                text = f.read()
                words = re.findall(r'\w+', text.lower())
                doc_lengths[filename] = len(words)

                for pos, word in enumerate(words):
                    inverted_index[word].append((filename, pos))

    return dict(inverted_index), doc_lengths

# --- Phase 2: TF-IDF Ranking ---
def compute_tf_idf(inverted_index, doc_lengths, total_docs):
    tfidf = defaultdict(dict)

    for term, postings in inverted_index.items():
        df = len(set([doc for doc, _ in postings]))
        idf = math.log10(total_docs / df)

        term_doc_freq = defaultdict(int)
        for doc, _ in postings:
            term_doc_freq[doc] += 1

        for doc in term_doc_freq:
            tf = term_doc_freq[doc] / doc_lengths[doc]
            tfidf[term][doc] = tf * idf

    return tfidf

def search(query, tfidf):
    query = query.lower()
    results = defaultdict(float)

    for word in query.split():
        if word in tfidf:
            for doc in tfidf[word]:
                results[doc] += tfidf[word][doc]

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return sorted_results

# --- Phase 3: Streamlit UI ---
st.title("📂 Mini Search Engine for Your Files")

folder_path = st.text_input("Enter folder path containing .txt files:", "docs")

if os.path.exists(folder_path):
    inverted_index, doc_lengths = build_inverted_index(folder_path)
    tfidf = compute_tf_idf(inverted_index, doc_lengths, len(doc_lengths))

    query = st.text_input("Enter your search query:")

    if query:
        results = search(query, tfidf)

        if results:
            st.subheader("Search Results:")
            for doc, score in results:
                st.write(f"📄 {doc} — Score: {score:.4f}")
        else:
            st.warning("No results found.")
else:
    st.warning("⚠️ Folder path doesn't exist. Please check and try again.")
