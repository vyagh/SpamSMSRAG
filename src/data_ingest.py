import pandas as pd
import re
from config import SPAM_CSV_PATH
from pathlib import Path

def ingest_data(file_path=SPAM_CSV_PATH):
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")
        
    df = pd.read_csv(file_path, encoding='latin-1')
    if not {'v1', 'v2'}.issubset(df.columns):
        raise ValueError("CSV must contain columns: v1, v2")
        
    df = df.rename(columns={'v1': 'label', 'v2': 'text'})
    df['text'] = df['text'].apply(lambda t: re.sub(r'<.*?>|\s+', ' ', t).strip())
    df['id'] = df.index
    df['metadata'] = df.apply(lambda r: {'label': r['label']}, axis=1)
    
    result_df = df[['id', 'text', 'metadata']].dropna()
    if result_df.empty:
        raise ValueError("No valid data after processing")
    return result_df

# TESTING CODE
if __name__ == "__main__":
    df = ingest_data()
    print(f"Loaded {len(df)} documents")
    print(f"Sample text: {df.iloc[0]['text'][:100]}...")