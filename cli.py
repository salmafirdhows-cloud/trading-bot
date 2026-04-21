import argparse
import logging
from client import get_client
from orders import place_order
from validators import validate_side, validate_order_type, validate_quantity
from logging_config import setup_logger

API_KEY = "demo_key"
API_SECRET = "demo_secret"

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        #  Validation
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        if args.type == "LIMIT" and args.price is None:
            raise ValueError("Price is required for LIMIT orders")

        client = get_client(API_KEY, API_SECRET)

        #  Log request
        logging.info(f"Order request: {vars(args)}")

        print("\n=== ORDER SUMMARY ===")
        print(vars(args))

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        #  Log response
        logging.info(f"Order response: {response}")

        print("\n=== RESPONSE ===")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

        print("\n Order placed successfully!")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print("\n Error:", str(e))


if __name__ == "__main__":
    main()