# 💰 Crypto Agent

The **Crypto Agent** is an AI-powered assistant designed to fetch and provide real-time cryptocurrency prices using the Binance API. It is built with Python and leverages the `agents` library for creating and running AI agents.

---

## 🚀 Features

- 📈 Fetches real-time cryptocurrency prices (default: BTC/USDT).
- 🛠️ Built with the `agents` library for AI agent creation.
- 🌐 Uses Binance API for accurate and up-to-date price data.
- ✅ Simple and easy-to-use interface.

---

## 📂 Project Structure
---

## 🛠️ Setup & Run

### 1. Clone Repo

```bash
git clone https://github.com/your-username/crypto-agent.git
cd crypto-agentpython -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt

python crypto_agent.py

📌 Example Output

When you run the agent, it will fetch the current price of Bitcoin 
(BTC/USDT) and display it:

🔗 API Used

Binance API

🙌 Acknowledgements

Thanks to the agents library for simplifying AI agent creation.
Binance API for providing real-time cryptocurrency data.
📌 Notes

Ensure you have an active internet connection to fetch data from the Binance API.
Modify the symbol parameter in the get_data function to fetch prices for other cryptocurrencies.
