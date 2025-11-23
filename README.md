🎨 AI Image App
<p align="center"> <b>AI-powered image generator built with Streamlit & Hugging Face Diffusion Models</b> </p> <p align="center"> Generate stunning images from text prompts, browse saved creations, and download them — all from a fast and intuitive web interface. </p>
🚀 Features

🔥 Text-to-Image Generation using Hugging Face diffusion models

🖼️ Built-in Image Gallery to view all generated images

📥 One-click downloads for any image

🧭 Multi-page Streamlit UI (Home, Generator, Gallery)

🎚️ Adjustable prompt settings

🔐 Secure API key handling using .env

📂 Project Structure
ai_image_app/
│── app.py                        # Main generator UI
│── pages/
│   │── home.py                   # Welcome / Home page
│   │── gallery.py                # Image gallery viewer
│
│── utils/
│   │── hf_client.py              # Hugging Face API client
│
│── assets/                       # Saved/generated images
│── .env                          # API tokens + output path
│── requirements.txt
│── README.md
│── .gitignore

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


Your browser will open at the app automatically.

🖼️ Image Gallery

All generated images are saved under:

./assets/


The Gallery page displays them in a clean 3-column grid with preview and download options.

📥 Example Prompt

A futuristic city floating in the clouds, ultra-detailed, cinematic lighting

🔧 Roadmap / Future Improvements

Add multiple model options (anime, photorealism, pixel art)

Image-to-image generation

Built-in image upscaling (Real-ESRGAN)

Prompt presets / templates

Rate limiting & error handling improvements

User-defined output folders

🪪 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute with attribution.
