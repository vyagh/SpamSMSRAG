from sentence_transformers import SentenceTransformer
from config import MODELS

def embed_chunks(chunks, model_name=MODELS['embedding']):
    model = SentenceTransformer(model_name)
    texts = [chunk[2] for chunk in chunks]
    chunk_ids = [chunk[1] for chunk in chunks]
    embeddings = model.encode(texts, batch_size=MODELS['batch_size'], show_progress_bar=True)
    return list(zip(chunk_ids, embeddings))

# TESTING CODE
if __name__ == "__main__":
    from data_ingest import ingest_data
    from custom_chunker import chunk_documents
    
    chunks = chunk_documents(ingest_data())
    embeddings = embed_chunks(chunks)
    print(f"Generated {len(embeddings)} embeddings")