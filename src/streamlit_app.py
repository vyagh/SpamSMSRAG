import streamlit as st
from app import get_qa_chain, ask_question

st.set_page_config(
    page_title="RAG Question Answering System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Question Answering System")

# Initialize session state for QA chain
if 'qa_chain' not in st.session_state:
    with st.spinner('Initializing the QA system...'):
        st.session_state.qa_chain = get_qa_chain()

# Create the input area
user_question = st.text_input("Ask your question:", placeholder="Type your question here...")

if user_question:
    with st.spinner('Thinking...'):
        # Get the answer
        result = st.session_state.qa_chain.invoke({"query": user_question})
        
        # Display the answer
        st.subheader("Answer:")
        st.write(result['result'])
        
        # Display sources
        st.subheader("Sources:")
        for doc in result['source_documents']:
            with st.expander(f"Source {doc.metadata.get('source', 'Unknown')}"):
                st.write(doc.page_content) 