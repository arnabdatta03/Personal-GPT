# 🧠 Personal GPT Assistant (Jarvis) using Google GenAI (Gemini)

A friendly and smart personal AI assistant named **GPT** built using the **Gemini model** from Google’s Generative AI. This assistant is designed to chat with you, provide helpful information, and respond in a conversational, friendly tone — just like a personal GPT.

---

## 🚀 Features

- 🤖 Built with **Google Gemini Pro** (Generative AI)
- 🔐 **API Key is secured** using `.env` file for safe configuration
- 🗨️ Maintains context with chat history
- 👨‍💻 Terminal-based real-time interaction
- 💬 Customizable assistant instructions (friendly, formal, fun, etc.)

---

## 🔧 Tech Stack

- Language: **Python 3.10+**
- Model: **Gemini Pro (google-generativeai)**
- Security: **dotenv** for API key protection
- CLI Interface for simplicity

---

## 📁 Folder Structure

## 📦 Installation & Setup

1. **Clone this repository**
git clone https://github.com/your-username/personal-gpt.git
cd personal-gpt
2. **Install dependencies**
pip install -r requirements.txt
3. **Create a .env file with your Gemini API key:**
GEMINI_API_KEY=your_actual_api_key_here
4. **Run the assistant**
uv run main.py

**📌 Limitations**

❌ No access to real-time data or news: The Gemini model does not fetch current data or browse the internet. It can only respond based on the knowledge it's trained on (up to mid-2023).

**🧠 It's best suited for:**

General Q&A
Productivity help
Personal reminders
Fun and contextual conversation

**🛡️ Safety & Security**

Your API key is stored safely using a .env file.
Make sure not to commit your .env file to any public repository.

**💡 Future Ideas**

Integrate voice (TTS + STT) for real Jarvis-like experience
Add GUI using Tkinter or Streamlit
Log conversations into a database
Generate responses in multiple languages

**🤝 Author**

Arnab Datta
Aspiring Data Analyst | Python & AI Enthusiast*