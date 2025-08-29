from output_data import OutputData, outDataclass 

from agents import Agent

guardrails = Agent(
    name="Guardial Agent",
    instructions="Act as a verification gatekeeper. Always confirm if the user is a GIAIC student before answering any of their queries.",
    tools=[],
    output_type=OutputData,
)

timing_guardrail = Agent(
    name="Guradial agent",
    instructions="check input is  not related to my class timing ",
    tools=[],
    output_type=outDataclass,
)

father_guardrail = Agent(
    name="Father Guardrail",
    instructions="""You are a father who decides if the child can run. "
        "Rule: If the temperature in the input is below 26°C, do not allow. """,
    tools=[],
)
