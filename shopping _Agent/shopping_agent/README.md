
# 🛒 Shopping Agent Backend (FastAPI + Gemini)

This is the **backend API** for the Shopping Agent project.  
It is built with **FastAPI** and powered by **Google Gemini (via OpenAI Agents SDK)**.  
The backend runs the **Shopping Agent** using the `Runner` and exposes an endpoint for frontend communication.

---

## 🚀 Features
- ✅ FastAPI server with CORS enabled  
- ✅ Integration with **Gemini API** through `config.py`  
- ✅ Shopping Agent implemented with `Runner`  
- ✅ Maintains simple conversation history (not production safe)  
- ✅ Clean JSON responses for frontend  

---

## 📂 Project Structure
```

├── agent.py         # Shopping agent 
├── config.py        # Gemini API key & config
├── main.py          # FastAPI server (this file)

````

---

## ⚡ API Endpoint

### `POST /agent`

**Request body:**
```json
{
  "message": "Find me a laptop under $500"
}
````

**Response:**

```json
{
  "response": "Here are 3 recommended laptops under $500..."
}
```

---

## 🛠️ Setup & Run

### 1. Clone Repo

```bash
git clone https://github.com/your-username/shopping-agent-backend.git
cd shopping-agent-backend
```

### 2. Create Virtual Env & Install

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

### 3. Add Environment Key

Make sure your **Gemini API key** is set inside `config.py`.

### 4. Run Server

```bash
uvicorn main:app --reload or fastapi run main.py
```

Server will be running on 👉 `http://127.0.0.1:8000`

---

## 🔗 Frontend Integration

* The backend is designed to be used with a **Next.js frontend**.
* Simply send a POST request from the frontend to `/agent` with the user’s message.

Example (frontend):

```ts
const response = await fetch("http://127.0.0.1:8000/agent", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: "Find shoes under $50" }),
});
const data = await response.json();
console.log(data.response);
```

---

## 📌 Notes

* Conversation history is stored in memory (not persistent).
* For production, consider a database or vector store for memory.
* Replace `allow_origins=["*"]` with specific domains in production.

---

## 🙌 Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/)
* [Google Gemini](https://ai.google.dev/)
* [OpenAI Agents SDK](https://pypi.org/project/openai-agents/)

---

✨ Built by [Muskan Fatima](https://github.com/muskan-fatim)

```
