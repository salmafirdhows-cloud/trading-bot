import random
import time

class MockClient:
    def futures_create_order(self, **kwargs):
        time.sleep(1)  # simulate API delay

        return {
            "orderId": random.randint(100000, 999999),
            "status": "FILLED" if kwargs.get("type") == "MARKET" else "NEW",
            "executedQty": str(kwargs.get("quantity")),
            "avgPrice": str(kwargs.get("price", 65000)),
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": kwargs.get("type")
        }

def get_client(api_key, api_secret):
    return MockClient()