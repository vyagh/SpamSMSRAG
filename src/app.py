import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain.chains import RetrievalQA
from config import GOOGLE_API_KEY, MODELS, DATA_DIR
from vector_store import load_vectorstore, index_embeddings, save_vectorstore
from custom_chunker import chunk_documents
from data_ingest import ingest_data
from embedder import embed_chunks
from pathlib import Path

def get_qa_chain():
    genai.configure(api_key=GOOGLE_API_KEY)
    model = ChatGoogleGenerativeAI(
        model=MODELS['llm'],
        google_api_key=GOOGLE_API_KEY,
        temperature=MODELS['temperature'],
        max_output_tokens=MODELS['max_tokens']
    )
    
    vectorstore_path = DATA_DIR / 'processed' / 'vectorstore'
    try:
        return RetrievalQA.from_chain_type(
            llm=model,
            chain_type="stuff",
            retriever=load_vectorstore(str(vectorstore_path)).as_retriever(search_kwargs={"k": MODELS['top_k']}),
            return_source_documents=True
        )
    except (FileNotFoundError, ValueError):
        if vectorstore_path.exists():
            vectorstore_path.unlink(missing_ok=True)
        chunks = chunk_documents(ingest_data())
        vectorstore = index_embeddings(chunks, embed_chunks(chunks))
        save_vectorstore(vectorstore, str(vectorstore_path))
        return RetrievalQA.from_chain_type(
            llm=model,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": MODELS['top_k']}),
            return_source_documents=True
        )

def ask_question(qa_chain, query):
    result = qa_chain.invoke({"query": query})
    print("\nAnswer:", result['result'])
    print("\nSources:")
    for doc in result['source_documents']:
        print(f"- {doc.page_content[:100]}...")


# TESTING CODE
if __name__ == "__main__":
    print("RAG system ready! (Type 'quit' to exit)")
    qa_chain = get_qa_chain()
    
    while True:
        query = input("\nYour question: ").strip()
        if query.lower() == 'quit': break
        if query: ask_question(qa_chain, query)