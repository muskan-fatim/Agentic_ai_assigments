from agents import Runner
from main import gate_kepper
from config import config
try:
 runner = Runner.run_sync(
    gate_kepper,
    input="I am a student of GIAIC, please allow me to enter the campus.",
    run_config=config
 )
 print(runner.final_output)
except Exception as e :
    print(f"An error occurred: {e}")


