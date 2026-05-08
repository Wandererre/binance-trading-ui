import argparse
import logging
from bot.client import BinanceTestnetClient

# Configure logging to file as requested
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=['BUY', 'SELL'])
    parser.add_argument("--type", required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # Replace these with your actual testnet keys!
    api_key = "YOUR_TESTNET_KEY"
    api_secret = "YOUR_SECRET_KEY"

    bot = BinanceTestnetClient(api_key, api_secret)
    
    print(f"--- Order Request Summary ---")
    print(f"Symbol: {args.symbol} | Side: {args.side} | Type: {args.type} | Qty: {args.quantity}")

    result = bot.place_order(args.symbol, args.side, args.type, args.quantity, args.price)

    if "error" in result:
        print(f"FAILED: {result['error']}")
    else:
        print(f"SUCCESS!")
        print(f"Order ID: {result.get('orderId')}")
        print(f"Status: {result.get('status')}")
        print(f"Avg Price: {result.get('avgPrice', 'N/A')}")

if __name__ == "__main__":
    main()