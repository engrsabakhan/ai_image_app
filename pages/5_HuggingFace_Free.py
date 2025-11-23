import streamlit as st
from PIL import Image
import os
from utils.hf_client import generate_image_hf
from dotenv import load_dotenv

load_dotenv()
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.title("🎨 Hugging Face Image Generator")

prompt = st.text_area("Enter your prompt:", "A magical forest with glowing trees")
num_images = st.slider("Number of images", 1, 4, 1)  # Generate 1–4 images

if st.button("✨ Generate Image"):
    with st.spinner("Generating... ⏳"):
        try:
            paths = generate_image_hf(prompt, num_images=num_images)
            for path in paths:
                st.image(Image.open(path), caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"❌ Error: {e}")
