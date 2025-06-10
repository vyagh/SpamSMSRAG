# RAG Assignment

This project implements a Retrieval-Augmented Generation (RAG) system using LangChain, Google Generative AI, and Streamlit.

## Streamlit Cloud Deployment

To deploy this app on Streamlit Cloud:

1. **Repository Structure**: Ensure your repository contains the following entry point:
   - `src/streamlit_app.py` (this is the main file to run on Streamlit Cloud)

2. **Deploying**:
   - Go to [Streamlit Cloud](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Set the main file path to: `src/streamlit_app.py`
   - Set Python version to 3.10 (in advanced settings)
   - Add your `GOOGLE_API_KEY` in the app's secrets (Settings > Secrets)

3. **Requirements**:
   - All dependencies are listed in `requirements.txt` in the root directory.

4. **Data**:
   - The app expects data in `src/data/raw/spam.csv` and a vectorstore in `src/data/processed/vectorstore/`.

5. **Running Locally**:
   - You can also run the app locally with:
     ```bash
     streamlit run src/streamlit_app.py
     ```

---

For more details, see the code and comments in each module. 