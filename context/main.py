from agents import Agent, RunContextWrapper, Runner, function_tool
from config import config
from pydantic import BaseModel

class UserInfo(BaseModel):
    name:str
    age:int
    school:str

user_context = UserInfo(name="Ayesha" , age=17,school="Degree college")

@function_tool
def context (ctx:RunContextWrapper):
    return f"your name is {ctx.context.name}"

agent = Agent(
    name="Context Agent",
    instructions="""You are a helpful assistant when user ask it's persnol detials like name age and" 
      school answer user using contxt tool""",
    tools=[context],
)

runner = Runner.run_sync(
    agent,
    "Hello, what is my name?",
    run_config=config,
    context=user_context,
)
print(runner.final_output)