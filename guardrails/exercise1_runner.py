from agents import Runner
from config import config
from main import timings

try:
 runner = Runner.run_sync(
    timings,
    input="want to change my class timings",
    run_config=config
 )
 print(runner.final_output)

except Exception as e :
    print(f"An error occurred: {e}")


