# app.py

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from utils_find_data_dir import find_data_directory
from PIL import Image

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

# Get the API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    st.error("Error: OPENAI_API_KEY not found in .env file")
    st.stop()

# Initialize the OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Find the data directory
data_dir = find_data_directory()

# Load the FAISS index
index_path = os.path.join(data_dir, "policy_faiss_index")
db = FAISS.load_local(index_path, embeddings)

def search_policy(query):
    results = db.similarity_search_with_score(query, k=1)
    if results:
        doc, score = results[0]
        return doc.page_content, doc.metadata["source"], score
    return None, None, None

def get_diagram_path(txt_filename):
    diagram_filename = txt_filename.replace('.txt', '_diagram.png')
    diagram_path = os.path.join(data_dir, diagram_filename)
    if os.path.exists(diagram_path):
        return diagram_path
    return None

st.set_page_config(layout="wide")

st.title("Corporate Policy Search")

query = st.text_input("Enter your search query:", key="search_input")
search_button = st.button("Search")

if search_button and query:
    policy_content, source_file, score = search_policy(query)
    
    if policy_content and source_file:
        
        diagram_path = get_diagram_path(source_file)
        if diagram_path:
            st.subheader("Policy Diagram")
            image = Image.open(diagram_path)
            st.image(image, use_column_width=True)
        else:
            st.warning("No diagram found for this policy.")
        
        st.subheader("Policy Content")
        st.markdown(f"<div style='font-size: 18px; height: 400px; overflow-y: scroll;'>{policy_content}</div>", unsafe_allow_html=True)
    else:
        st.warning("No matching policy found.")

