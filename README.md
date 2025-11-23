🎨 <b>AI Image App</b>
<p align="center"><b>AI-powered image generator built with Streamlit & Hugging Face Diffusion Models</b></p> <p align="center">Generate stunning images from text prompts, browse saved creations, and download them — all from a fast and intuitive web interface.</p></br>
__________________________________________________________________________________________________________________________<br>

🚀 <b>Features</br>
 <p>🔥Text-to-Image generation using Hugging Face diffusion models</p>
 <p>🖼️Built-in Image Gallery to view all generated images</p>
 <p>📥One-click image downloads</p>
 <p>🧭Multi-page Streamlit UI (Home, Generator, Gallery)</p>
 <p>🎚️Adjustable prompt settings</p>
 <p>🔐Secure API key handling using .env</p>
__________________________________________________________________________________________________________________________<br>

📂 <b>Project Structure</b>

<img width="174" height="277" alt="image" src="https://github.com/user-attachments/assets/d6db9cc4-1c6b-4ee5-b06f-8de92da40b69"/>
<br>
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

__________________________________________________________________________________________________________________________<br>

🛠️ <b>Built With</b>

<b>1</b> Python

<b>2</b> Streamlit

<b>3</b> Hugging Face Diffusers / API

<b>4</b> Pillow

<b>5</b> Requests

<b>6</b> python-dotenv
__________________________________________________________________________________________________________________________<br>
📦 <b>Installation</b><br>
1️⃣ Clone the repository
<code>git clone https://github.com/YOUR_USERNAME/ai_image_app.git
cd ai_image_app</code>

2️⃣ Create a virtual environment
python -m venv .venv

3️⃣ Activate the environment

<b>Windows</b>

.venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt
__________________________________________________________________________________________________________________________<br>
🔑 <b>Environment Variables</b>

Create a .env file:

HUGGINGFACE_TOKEN=your_hf_token_here
OUTPUT_DIR=./assets
__________________________________________________________________________________________________________________________<br>
▶️ <b>Run the App</b>
streamlit run app.py


Your browser will open automatically.
__________________________________________________________________________________________________________________________<br>
🖼️ <b>Image Gallery</b>

All generated images are saved in:

./assets/

__________________________________________________________________________________________________________________________<br>
📥 <b>Example Prompt</b>
A futuristic city floating in the clouds, ultra-detailed, cinematic lighting
__________________________________________________________________________________________________________________________<br>
🔧
🪪 <b>License</b>

This project is licensed under the MIT License.
Free to use, modify, and distribute with attribution.
__________________________________________________________________________________________________________________________<br>
