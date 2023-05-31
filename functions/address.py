import requests
from environs import Env
import time
import json
from binance.client import Client
from binance.client import Client 


env = Env()
env.read_env()
api_key = env.str('BINANCE_KEY')
api_secret = env.str('BINANCE_SECRET_KEY')

client = Client(api_key, api_secret, testnet=True)
print(client.create_test_order)


