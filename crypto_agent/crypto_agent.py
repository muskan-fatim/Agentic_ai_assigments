import httpx
from agents import Agent, function_tool, Runner
from config import config

@function_tool
def get_data(symbol: str = "BTCUSDT") -> str:
    """
    Fetch current cryptocurrency price from Binance.
    Default: BTC/USDT.
    """
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = httpx.get(url)
        response.raise_for_status()
        data = response.json()
        return f"{data['symbol']} price is {data['price']} USDT"
    except Exception as e:
        return f"Error fetching data: {e}"

# Create the agent
crypto_agent = Agent(
    name="Crypto Agent",
    instructions="You are a crypto expert that gives the current rate of cryptocurrency using Binance API.",
    tools=[get_data],
)

# Run synchronously
runner = Runner.run_sync(
    crypto_agent,
    "What is the current price of bitcoin?",
    run_config=config,
)

print(runner.final_output)
