from agents import Agent 
from input_guardrails import giaic_student_checker,class_timings_guardrail , temperature_checker

gate_kepper = Agent (
    name="Gate Keeper",
    instructions="you are geetkepper who give entery to giaic students and  greet them",
    tools=[],
    input_guardrails=[giaic_student_checker],
) 

timings = Agent(
    name = "Main Agent",
    instructions = "give me the details about governor it intiative classes",
    tools = [],
    input_guardrails=[class_timings_guardrail],
)

father_agent = Agent(
    name="Father Agent",
    instructions="You are a father who does not allow his child to run if the temperature is below 26°C.",
    tools=[],
    input_guardrails=[temperature_checker],
)
