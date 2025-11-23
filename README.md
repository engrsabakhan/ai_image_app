🎨 AI Image App
<p align="center"><b>AI-powered image generator built with Streamlit & Hugging Face Diffusion Models</b></p> <p align="center">Generate stunning images from text prompts, browse saved creations, and download them — all from a fast and intuitive web interface.</p>
🚀 <b>Features</b>

🔥 Text-to-Image generation using Hugging Face diffusion models
🖼️ Built-in Image Gallery to view all generated images
📥 One-click image downloads
🧭 Multi-page Streamlit UI (Home, Generator, Gallery)
🎚️ Adjustable prompt settings
🔐 Secure API key handling using .env

📂 <b>Project Structure</b>
<img width="174" height="277" alt="image" src="https://github.com/user-attachments/assets/d6db9cc4-1c6b-4ee5-b06f-8de92da40b69" />
🛠️ <b>Built With</b>

Python

Streamlit

Hugging Face Diffusers / API

Pillow

Requests

python-dotenv

📦 <b>Installation</b>
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/ai_image_app.git
cd ai_image_app

2️⃣ Create a virtual environment
python -m venv .venv

3️⃣ Activate the environment

Windows

.venv\Scripts\activate


macOS / Linux

source .venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

🔑 <b>Environment Variables</b>

Create a .env file:

HUGGINGFACE_TOKEN=your_hf_token_here
OUTPUT_DIR=./assets

▶️ <b>Run the App</b>
streamlit run app.py


Your browser will open automatically.

🖼️ <b>Image Gallery</b>

All generated images are saved in:

./assets/


Displayed in a clean 3-column grid with preview + download options.

📥 <b>Example Prompt</b>
A futuristic city floating in the clouds, ultra-detailed, cinematic lighting

🔧 <b>Roadmap / Future Improvements</b>

Multiple model options (anime, photorealism, pixel art)

Image-to-image generation

Built-in upscaling (Real-ESRGAN)

Prompt presets / templates

Rate-limit & error-handling improvements

Custom output directories

🪪 <b>License</b>

This project is licensed under the MIT License.
Free to use, modify, and distribute with attribution.
