# 🤖 Ultra Mind AI

An AI-powered chatbot built with **FastAPI**, **Google Gemini API**, and a modern **HTML, CSS & JavaScript** frontend.

Ultra Mind AI provides intelligent conversational responses using Google's Gemini model through a clean and responsive web interface.

## ✨ Features

- 🤖 Powered by Google Gemini AI
- ⚡ FastAPI backend
- 🎨 Modern and responsive UI
- 💬 Real-time chat interface
- ⌨️ Press Enter to send messages
- 🔒 API Key secured using `.env`
- 🌐 REST API architecture
- 📱 Mobile-friendly design
- 🚀 Easy to deploy

---

## 🛠 Tech Stack

### Backend
- FastAPI
- Google GenAI SDK
- Python
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript (ES6)

### AI Model
- Gemini 2.5 Flash

---

## 📂 Project Structure

```text
UltraMind-AI/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── .gitignore
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/UltraMind-AI.git

cd UltraMind-AI
```

---

### 2️⃣ Install dependencies

```bash
cd backend

pip install -r requirements.txt
```

---

### 3️⃣ Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

### 4️⃣ Run the backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

### 5️⃣ Run the frontend

Open the `frontend` folder using **VS Code Live Server**

or

```bash
cd frontend

python -m http.server 5500
```

Then open

```
http://127.0.0.1:5500
```

---

## 📡 API Endpoint

### POST `/chat`

#### Request

```json
{
  "message": "Hello AI!"
}
```

#### Response

```json
{
  "response": "Hello! How can I help you today?"
}
```

---

## 🔒 Environment Variables

Create a `.env` file inside the backend folder.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

> **Note:** Never upload your `.env` file to GitHub.

---

## 🚀 Future Improvements

- 🎤 Voice Input
- 🔊 Text-to-Speech
- 📄 Chat History
- 📎 File Upload Support
- 🌙 Dark / Light Theme
- 🧠 Streaming Responses
- 📝 Markdown Rendering
- 💾 Save Conversations
- 🔑 User Authentication

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Debojit Ghosh**

Aspiring AI Engineer | Python Developer | FastAPI Enthusiast

- GitHub: https://github.com/Debojitghosh-it
- LinkedIn: *(Add your LinkedIn profile URL here)*

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork it

🛠️ Contribute

Sharing feedback is always appreciated!
