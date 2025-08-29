from agents import Runner
from main import father_agent
from config import config

try:
    runner = Runner.run_sync(
        father_agent,
        input="Dad, can I go for a run?",
        run_config=config,
        context={"temperature": 26},  
    )
    print("Case 1 Output:", runner.final_output)

except Exception as e:
    print(f"InputGuardRailTripwireTriggered: {e}")
