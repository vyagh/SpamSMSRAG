from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import MODELS, DATA_DIR
from pathlib import Path

def index_embeddings(chunks, embeddings, embedding_model=MODELS['embedding']):
    texts, metadatas = zip(*[(chunk[2], chunk[3]) for chunk in chunks])
    return FAISS.from_texts(texts, HuggingFaceEmbeddings(model_name=embedding_model), metadatas=metadatas)

def save_vectorstore(vectorstore, path=None):
    path = Path(path or DATA_DIR / 'processed' / 'vectorstore')
    path.parent.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(path))
    return path

def load_vectorstore(path=None, embedding_model=MODELS['embedding']):
    path = str(path or DATA_DIR / 'processed' / 'vectorstore')
    return FAISS.load_local(path, HuggingFaceEmbeddings(model_name=embedding_model), allow_dangerous_deserialization=True)

# TESTING CODE
if __name__ == "__main__":
    from data_ingest import ingest_data
    from custom_chunker import chunk_documents
    from embedder import embed_chunks
    
    chunks = chunk_documents(ingest_data())
    vectorstore = index_embeddings(chunks, embed_chunks(chunks))
    save_path = save_vectorstore(vectorstore)
    print(f"Vector store created and saved to: {save_path}")