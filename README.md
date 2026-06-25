# AI Chatbot with Memory (Groq API)

## 📌 Overview

This project is a terminal-based conversational AI chatbot built with Python and the Groq API. The chatbot maintains conversation memory during the session, allowing it to respond based on previous messages. The project follows a modular structure by separating the chatbot logic from the application entry point.

---

## 🚀 Features

* Real-time AI responses using Groq API
* LLaMA 3.1 language model
* Conversation memory
* Sliding window memory (keeps the latest 10 messages)
* Environment variable support using `.env`
* Modular project structure
* Built-in commands:

  * `memory` – View conversation history
  * `clear` – Clear conversation memory
  * `exit` – Exit the chatbot

---

## 📁 Project Structure

```text
custom-ai-chatbot/
│
├── main.py
├── chatbot.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

> **Note:** The `.env` file is required locally but is not uploaded to GitHub.

---

## 🧠 Technology Stack

* Python 3.12
* Groq API
* LLaMA 3.1 Instant
* python-dotenv

---

## ▶️ Installation

```bash
git clone https://github.com/your-username/custom-ai-chatbot.git
cd custom-ai-chatbot
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💡 Available Commands

| Command  | Description                    |
| -------- | ------------------------------ |
| `memory` | Display conversation history   |
| `clear`  | Clear the current conversation |
| `exit`   | Close the chatbot              |

---

## 📄 License

This project was created for learning purposes and portfolio development.

