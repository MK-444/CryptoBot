from datetime import datetime, timedelta
from decimal import Decimal
from random import randint

# from binance import AsyncClient
from environs import Env

env = Env()
env.read_env()

api_key = env.str('BINANCE_KEY')
api_secret = env.str('BINANCE_SECRET_KEY')

from binance.client import Client

client = Client("api_key", "api_secret")

symbol = "ETHBTC"

price = client.get_symbol_ticker(symbol=symbol)

price_from_binance = float(price['price'])
# print(price_from_binance)
# print("Current price of is {:.2f}".format(price))