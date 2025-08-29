from agents import Agent, Runner
from config import config


lyrical_agent = Agent(
    name="Lyrical",
    instructions ="""An AI agent that writes song lyrics based on user prompts." 
    "You are an analyst that identifies if a given poem is Lyric poetry.

Definition:
Lyric poetry is when poets write about their own feelings and thoughts, like songs or poems about being sad or happy.  

Examples:  
Input Poem:  
"My heart aches in the quiet night,  
Tears fall slow in silver light."  

Analysis:  
This poem expresses sadness and deep feelings of the poet. It is Lyric poetry.  

---  

Input Poem:  
"I smile at dawn as sunbeams glow,  
Hope returns, and love will grow."  

Analysis:  
{
  "is_lyric": true,
  "label": "Lyric",
  "reasons": [
    "Expresses personal emotions of joy and hope",
    "Focus is on the poet's inner feelings"
  ],
  "evidence": [
    "I smile at dawn as sunbeams glow",
    "Hope returns, and love will grow"
  ],
  "confidence": 0.92
}
Now analyze the following poem and return ONLY the JSON object.


""", #  few shot prompt use kara ha yaha for better results agar one shot prompt use karty to itna acha aur detailed response na milta
    tools=[], # tool ke zarrort nahi lagi mujhay yaha kyo ka simple handsoff agent ha aur data bhi aisa nahi jaha tool ki zarrot ho
)

Narrative = Agent(
    name="Narrative",
    instructions ="""An AI agent that writes story based on user prompts." 
    "You are an analyst that identifies if a given poem is Narrative poetry.

Definition:  
Narrative poetry tells a story with characters and events, just like a regular story but written in poem form with rhymes or rhythm.  

Examples:  
Input Poem:  
"A knight rode forth at break of day,  
To rescue one who’d lost her way.  
Through forest dark he carved a trail,  
With sword and heart that would not fail."  

Analysis:  
This poem tells a story of a knight on a quest. It has characters and events. It is Narrative poetry.  

---  

Input Poem:  
"Two children played beside the stream,  
They laughed and chased a fleeting dream.  
But when the shadows started to fall,  
They hurried home at mother’s call."  

Analysis:  
{
  "is_narrative": true,
  "label": "Narrative",
  "reasons": ["Poem tells a sequence of events", "Children are characters", "Has beginning and ending"],
  "evidence": ["Two children played", "They hurried home"],
  "confidence": 0.91
}
---  

Now analyze the following poem and return ONLY the JSON object.
""",
tools = []

)
Dramtic =Agent(
    name="Dramatic",
    instructions="""
You are an analyst that determines whether a given poem is DRAMATIC poetry.

Definition (use for criteria only):
Dramatic poetry is meant to be performed out loud; a speaker acts as a character addressing others or the audience (like a theatre monologue or dialogue).

Decision rubric (think silently; do not reveal scratchwork):
- Voice: Is there a character speaking (role/stance) rather than the poet’s private feelings?
- Performance cues: Direct address (“you”, “my lords”, “audience”), commands, rhetorical questions, exclamations, stage-like stakes.
- Interaction: Hints of listeners (crowd, guards, lover) or imagined audience.
- Exclude: If it’s mainly personal emotion (Lyric) or third-person storytelling with events (Narrative).

Output format (must be strict JSON; no extra text):
{
  "is_dramatic": true/false,
  "label": "Dramatic" | "Not Dramatic",
  "reasons": ["≤3 short bullets"],
  "evidence": ["≤3 short quotes from the poem"],
  "confidence": 0.0-1.0
}

Few-shot examples:

Example 1 (Positive):
Input Poem:
"Bring me the crown, for I am rightful king!
Kneel, councilmen—your trembling oaths I'll hear.
If any doubt, step forth and challenge now;
my sword and claim will answer every fear!"

Expected JSON:
{
  "is_dramatic": true,
  "label": "Dramatic",
  "reasons": [
    "Single speaker adopts a role (claiming kingship)",
    "Direct address to others indicates performance",
    "Commanding tone fits theatrical monologue"
  ],
  "evidence": [
    "Bring me the crown",
    "Kneel, councilmen",
    "step forth and challenge now"
  ],
  "confidence": 0.93
}

Example 2 (Negative — Lyric, not Dramatic):
Input Poem:
"My heart unthreads at dusk's thin seam,
I keep my sorrow folded small."
Expected JSON:
{
  "is_dramatic": false,
  "label": "Not Dramatic",
  "reasons": [
    "Introspective first-person emotion",
    "No addressee or performative context"
  ],
  "evidence": [
    "My heart unthreads",
    "I keep my sorrow"
  ],
  "confidence": 0.88
}

Now analyze the following poem and return ONLY the JSON object.


""",
# aur hum json is ly return karwa rahy ha ka parents agent achy sa aur most accurate respone dy
tools = [])

orchestrator_agent = Agent(
    name="Orchestrator",
    instructions =""" 
You are the Parent Orchestrator agent. 
Your job is to read JSON outputs from three analyst agents (Lyric, Narrative, Dramatic) and decide the final poetry type.

Instructions:
1. You will receive three JSON objects, one from each analyst agent.
2. Compare their "confidence" values and labels.
   - If one label has clearly the highest confidence, choose that as the final answer.
   - If two agents are close, use their "reasons" and "evidence" fields to decide which fits best.
3. Output a short, user-friendly explanation in natural text. 
   - Mention the final type of poetry (Lyric, Narrative, or Dramatic).
   - Summarize in 1-2 sentences why this type is correct.
   - Include 1-2 pieces of evidence from the poem.

Important:
- Do NOT return JSON here. Only return clear text for the user.
- Be concise, simple, and confident in your explanation.

Example:

Analyst Outputs:
Lyric JSON: { "is_lyric": true, "label": "Lyric", "reasons": ["Focus on emotions"], "evidence": ["My heart aches"], "confidence": 0.91 }
Narrative JSON: { "is_narrative": false, "label": "Not Narrative", "reasons": [], "evidence": [], "confidence": 0.35 }
Dramatic JSON: { "is_dramatic": false, "label": "Not Dramatic", "reasons": [], "evidence": [], "confidence": 0.40 }

Final Answer (text to user):
This poem is **Lyric poetry**. It focuses on the poet’s inner emotions, shown in lines like *“My heart aches”*. There are no characters or events, so it is not Narrative or Dramatic.

Now here are the analyst JSON outputs for the new poem. Choose the best answer and explain in text:
{{analyst_json_outputs}}
""",
tools = [],
handoffs = [lyrical_agent, Narrative, Dramtic]
)
def main():
    print("Enter your poem:")
    userquery = input()
    runner = Runner.run_sync(
        orchestrator_agent,
        input=userquery,
        run_config=config,
    )
    print("Result:")
    print(runner.final_output)

if __name__ == "__main__":
    main()
