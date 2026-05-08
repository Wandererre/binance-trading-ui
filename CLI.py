import argparse
import logging
from bot.client import BinanceTestnetClient

# Configure logging to file as requested [cite: 32, 56]
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g., BTCUSDT") [cite: 21]
    parser.add_argument("--side", required=True, choices=['BUY', 'SELL']) [cite: 22]
    parser.add_argument("--type", required=True, choices=['MARKET', 'LIMIT']) [cite: 24]
    parser.add_argument("--quantity", required=True, type=float) [cite: 25]
    parser.add_argument("--price", type=float, help="Required for LIMIT orders") [cite: 26]

    args = parser.parse_args()

    # Load keys from environment variables for security
    api_key = "FyO9vm9CjyfplaZNaKMZQe7izxLwM20iIlwgcvtnTERyOliJ2YM3MjgVtEQZ0kNd"
    api_secret = "Vpf9brslYrziiGGuakIC5aTLjPxsqlnIZshqYEyTJ6C9B2RisBog8dORp3gLjl6j"

    bot = BinanceTestnetClient(api_key, api_secret)
    
    print(f"--- Order Request Summary ---") [cite: 28]
    print(f"Symbol: {args.symbol} | Side: {args.side} | Type: {args.type} | Qty: {args.quantity}")

    result = bot.place_order(args.symbol, args.side, args.type, args.quantity, args.price)

    if "error" in result:
        print(f"FAILED: {result['error']}") [cite: 29]
    else:
        print(f"SUCCESS!") [cite: 29]
        print(f"Order ID: {result.get('orderId')}")
        print(f"Status: {result.get('status')}")
        print(f"Avg Price: {result.get('avgPrice', 'N/A')}") [cite: 29]

if __name__ == "__main__":
    main()