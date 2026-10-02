import os, threading, time, pandas as pd
from binance.client import Client
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "BIBLE BOT LIVE 24/7"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_web, daemon=True).start()

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
client = Client(API_KEY, API_SECRET)

SYMBOL="BTCUSDT"
print("BIBLE BOT CLOUD LIVE")
while True:
  try:
    klines = client.get_klines(symbol=SYMBOL, interval=Client.KLINE_INTERVAL_15MINUTE, limit=50)
    print("Bot running, price check OK")
    time.sleep(60)
  except Exception as e:
    print(e)
    time.sleep(10)
