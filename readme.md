# Binance Futures Testnet Trading Bot

This is a simplified Python command-line application that places orders on the Binance Futures Testnet (USDT-M).

## Setup Steps
1. Clone this repository.
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Open CLI.py and replace YOUR_TESTNET_KEY and YOUR_TESTNET_SECRET with your actual Binance Testnet API credentials.

## How to Run Examples

**To place a MARKET order:**
```bash
python CLI.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005
```

**To place a LIMIT order:**
```bash
python CLI.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.005 --price 90000
```

## Assumptions
* The user has an active Binance Futures Testnet account.
* Python 3.x is installed on the user's machine.
* The script outputs logs to trading_bot.log automatically.