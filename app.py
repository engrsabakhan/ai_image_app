import streamlit as st

st.set_page_config(page_title="🎨 AI Image Studio", layout="wide")
st.title("🎨 AI Image Studio")

st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to select pages.")

st.write("""
Welcome! This multi-page app demonstrates AI image generation with Hugging Face Stable Diffusion.
- Page 1: Home
- Page 2: Generate Images (Hugging Face)
- Page 3: Gallery
""")
