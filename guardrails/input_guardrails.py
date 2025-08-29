from agents import  GuardrailFunctionOutput,  RunContextWrapper,Runner, input_guardrail , Agent ,InputGuardrailTripwireTriggered
from guardrail import guardrails, timing_guardrail 
from config import config

@input_guardrail
async def giaic_student_checker( ctx: RunContextWrapper, agent:Agent , input):
    result = await Runner.run(guardrails, input, context=ctx.context , run_config = config)

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered= not result.final_output.is_giaic_student,
    )

@input_guardrail
async def class_timings_guardrail( ctx: RunContextWrapper, agent:Agent , input):
    result = await Runner.run(timing_guardrail, input, context=ctx.context , run_config = config)

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=result.final_output.is_realted_to_timing,
    )

from agents import GuardrailFunctionOutput, RunContextWrapper, input_guardrail, Agent

@input_guardrail
async def temperature_checker(ctx: RunContextWrapper, agent: Agent, input: str):
    """
    Guardrail: Allow child to run if temperature < 26°C.
               Stop child if temperature >= 26°C.
    """
    temperature = ctx.context.get("temperature", None)

    if temperature is None:
        return GuardrailFunctionOutput(
            output_info="No temperature provided in context.",
            tripwire_triggered=True,
        )

    if temperature < 26:
        return GuardrailFunctionOutput(
            output_info=f"Temperature is {temperature}°C ✅ Father says: You may run.",
            tripwire_triggered=False,  # no block
        )

    return GuardrailFunctionOutput(
        output_info=f"Temperature is {temperature}°C ❌ Father says: No running!",
        tripwire_triggered=True,  # block
    )
