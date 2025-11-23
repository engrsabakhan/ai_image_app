🎨 AI Image App
<p align="center"><b>AI-powered image generator built with Streamlit & Hugging Face Diffusion Models</b></p> <p align="center">Generate stunning images from text prompts, browse saved creations, and download them — all from a fast and intuitive web interface.</p>
🚀 Features

🔥 Text-to-Image generation using Hugging Face diffusion models
🖼️ Built-in Image Gallery to view all generated images
📥 One-click download for any image
🧭 Multi-page Streamlit UI (Home, Generator, Gallery)
🎚️ Adjustable prompt settings
🔐 Secure API key handling via .env
📁 Auto-save all generated images to /assets

📂 Project Structure
<img width="174" height="277" alt="image" src="https://github.com/user-attachments/assets/d6db9cc4-1c6b-4ee5-b06f-8de92da40b69" />
ai_image_app/
│── app.py
│── pages/
│   ├── home.py
│   ├── generator.py
│   └── gallery.py
│── utils/
│   └── hf_client.py
│── assets/
│── requirements.txt
│── .env
│── README.md

🛠️ Built With

Python

Streamlit

Hugging Face Diffusers / API

Pillow

Requests

python-dotenv

📦 Installation
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

🔑 Environment Variables

Create a .env file in the project root:

HUGGINGFACE_TOKEN=your_hf_token_here
OUTPUT_DIR=./assets

▶️ Run the App

Start Streamlit:

streamlit run app.py


Your browser will open automatically.

🖼️ Image Gallery

All generated images are saved inside:

./assets/


The Gallery page displays them in a 3-column grid with preview & download options.

📥 Example Prompt
A futuristic city floating in the clouds, ultra-detailed, cinematic lighting

🔧 Roadmap / Future Improvements

⬜ Multiple model styles (anime, realism, pixel art)
⬜ Image-to-image generation
⬜ Built-in upscaling (Real-ESRGAN)
⬜ Prompt presets
⬜ Improved rate limiting / error handling
⬜ User-defined output directory

🪪 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute with attribution.
