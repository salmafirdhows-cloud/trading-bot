# Binance Futures Trading Bot (CLI)

##  Overview
This is a Python-based CLI trading bot that simulates placing MARKET and LIMIT orders on Binance Futures Testnet.

##  Setup
1. Clone the repository
2. Navigate into the project folder
3. Run the CLI commands below

##  Usage

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Output
- Order summary
- Order response (orderId, status, executedQty, avgPrice)
- Success / failure message

##  Logs
All API requests, responses, and errors are logged in:
bot.log

##  Note
The application is designed with a modular client layer.

Due to access restrictions on Binance Futures Testnet (KYC requirement),
a mock client is used to simulate order placement.

The architecture supports seamless switching to the real Binance API
by updating the client implementation.