import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.title("🖼️ Gallery")

image_files = [f for f in os.listdir(OUTPUT_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

if not image_files:
    st.info("No images yet. Generate one from the Hugging Face page!")
else:
    st.success(f"Found {len(image_files)} image(s) in {OUTPUT_DIR}")
    cols = st.columns(3)
    for i, file in enumerate(sorted(image_files, reverse=True)):
        with cols[i % 3]:
            path = os.path.join(OUTPUT_DIR, file)
            st.image(path, use_column_width=True)
            st.download_button("Download", data=open(path, "rb"), file_name=file, mime="image/png")
