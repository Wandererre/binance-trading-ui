import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

class BinanceTestnetClient:
    def __init__(self, api_key, api_secret):
        # Use the testnet base URL provided in the task [cite: 11]
        self.client = Client(api_key, api_secret, testnet=True)
        self.logger = logging.getLogger(__name__)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity
            }
            
            if order_type.upper() == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders.") [cite: 26]
                params['price'] = price
                params['timeInForce'] = 'GTC'  # Good 'Til Canceled

            # Placing a futures order [cite: 18]
            self.logger.info(f"Sending {order_type} {side} request for {symbol}") [cite: 32]
            response = self.client.futures_create_order(**params)
            return response

        except BinanceAPIException as e:
            self.logger.error(f"API Error: {e.message}") [cite: 32, 63]
            return {"error": e.message}
        except Exception as e:
            self.logger.error(f"Unexpected Error: {str(e)}") [cite: 32]
            return {"error": str(e)}