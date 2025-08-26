from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config import config   # this already loads GEMINI_API_KEY
from agents import Runner
from agent import Shopping

app = FastAPI()

# 👇 Allow both localhost and 127.0.0.1
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    message: str

# 👇 simple global memory (for testing only, not production safe)
conversation_history = []

@app.post("/agent")
async def run_agent(data: UserMessage):
    print("Incoming from frontend:", data.message, type(data.message))

    # ✅ use Runner with Gemini (already set in config.py)
    result = await Runner.run(
        starting_agent=Shopping,
        input=str(data.message),   # force to string
        context={"history": conversation_history},
        run_config=config,             # 👈 IMPORTANT: pass Gemini config here
    )

    print("Runner result:", result, type(result))
    return {"response": str(result.final_output)}
