import streamlit as st
import logging
import warnings
import os

# Configure logging and warnings
logging.getLogger("streamlit.watcher.local_sources_watcher").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Configure Streamlit
st.set_page_config(page_title="RAG Question Answering", layout="wide")

# Import RAG components
from app import get_qa_chain

# Initialize session state
if 'qa_chain' not in st.session_state:
    with st.spinner("Initializing RAG system..."):
        st.session_state.qa_chain = get_qa_chain()

# Title
st.title("RAG Question Answering System")

# Question input
query = st.text_input("Enter your question:", placeholder="What is a spam message?")

# Process question when submitted
if query:
    with st.spinner("Thinking..."):
        try:
            result = st.session_state.qa_chain.invoke({"query": query})
            
            # Display answer
            st.subheader("Answer")
            st.write(result['result'])
            
            # Display sources
            st.subheader("Sources")
            for doc in result['source_documents']:
                st.markdown(f"- {doc.page_content[:200]}...")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}") 