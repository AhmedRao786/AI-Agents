# # pip install openai-agents
# # pip install python-dotenv
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# from dotenv import load_dotenv
# import os

# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# print(gemini_api_key)
# # Check if the API key is present; if not, raise an error
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# #Reference: https://ai.google.dev/gemini-api/docs/openai
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # Crypto Agent
# Crypto = Agent(
#     name = 'Crypto Agent',
#     instructions= 
#     """You are a Crypto Intelligence Agent.
# Your role is to monitor, analyze, summarize, and respond to crypto-related content in real-time.
# You help users make informed decisions based on data, trends, risk signals, and market sentiment."""
# )

# response = Runner.run_sync(
#     Crypto,
#     input = input('Write a 2 paragraphs on Generative AI..'),
#     run_config = config
#     )
# print(response.final_output)




import requests

def show_top_10_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        response = requests.get (url)
        response.raise_for_status()
        data = response.json()

        print ("\n 10 Top 10 Crypto Coin Prices on Binance: \n")
        for coin in data[:10]:
            print(f" • {coin['symbol']}: {coin['price']} USDT")
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching top 10 coin prices:", e)

def show_specific_coin_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n💰 Current Price of {symbol.upper()}: {data['price']} USDT")
        else:
            print("❗ Invalid coin symbol or not available on Binance.")
    except requests.exceptions.RequestException as e:
        print(" ❌ Error fetching specific coin price:", e)

def main():
    print("📊 Live Crypto Price Agent using Binance API\n")

    # Step 1: Show top 10 coin prices
    show_top_10_prices ()

    # Step 2: Take user input for specific coin
    while True:
        user_input = input("\n🔎 Enter a coin symbol (e.g., BTUSDT) or type 'exit' to quit: ").strip()
        if user_input. lower() == 'exit':
            print("👋 Exiting program. Stay updated with Crypto")
            break
        if user_input:
            show_specific_coin_price(user_input)
        else:
            print("❗ Please enter a valid coin symbol.")

if __name__ == "__main__":
    main()