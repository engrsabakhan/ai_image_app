# utils/hf_client.py

import os
import uuid
import base64
import requests
from pathlib import Path
from dotenv import load_dotenv
import certifi  # SSL verification
import time     # optional delay to avoid rate limits

# Load environment variables
load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEFAULT_MODEL = "runwayml/stable-diffusion-v1-5"
# Updated Hugging Face router endpoint
API_URL_BASE = "https://router.huggingface.co/hf-inference/models/"

HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"} if HUGGINGFACE_TOKEN else {}

def _save_bytes_to_file(b: bytes, ext: str = "png") -> str:
    """Save image bytes to OUTPUT_DIR and return path"""
    filename = f"{uuid.uuid4().hex}.{ext}"
    path = Path(OUTPUT_DIR) / filename
    with open(path, "wb") as f:
        f.write(b)
    return str(path)

def generate_image_hf(prompt: str, num_images: int = 1, model: str = DEFAULT_MODEL,
                      width: int = 512, height: int = 512, guidance_scale: float = 7.5):
    """Generate images using Hugging Face Stable Diffusion"""

    if not HUGGINGFACE_TOKEN:
        raise RuntimeError("HUGGINGFACE_TOKEN not set in .env")

    url = API_URL_BASE + model
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True},
        "parameters": {
            "num_inference_steps": 30,
            "guidance_scale": guidance_scale,
            "width": width,
            "height": height,
            "num_images_per_prompt": num_images
        },
    }

    headers = HEADERS.copy()
    headers["Accept"] = "application/json"

    # Optional small delay to avoid free-tier rate limits
    time.sleep(1)

    # Make API request with SSL fix
    resp = requests.post(url, headers=headers, json=payload, timeout=180, verify=certifi.where())

    if resp.status_code != 200:
        try:
            j = resp.json()
            raise RuntimeError(f"Hugging Face API error {resp.status_code}: {j}")
        except Exception:
            raise RuntimeError(f"Hugging Face API error {resp.status_code}: {resp.text}")

    data = resp.json()
    output_paths = []

    # Handle returned base64 images
    items = data if isinstance(data, list) else [data]
    for item in items:
        if isinstance(item, dict):
            for key in ("image", "generated_image", "b64_json", "image_base64", "png"):
                if key in item and item[key]:
                    b64 = item[key]
                    if b64.startswith("data:"):
                        b64 = b64.split(",", 1)[1]
                    decoded = base64.b64decode(b64)
                    path = _save_bytes_to_file(decoded, ext="png")
                    output_paths.append(path)
                    break
        elif isinstance(item, str):
            b64 = item
            if b64.startswith("data:"):
                b64 = b64.split(",", 1)[1]
            decoded = base64.b64decode(b64)
            path = _save_bytes_to_file(decoded, ext="png")
            output_paths.append(path)

    if not output_paths:
        raise RuntimeError("No image returned from model")

    return output_paths
