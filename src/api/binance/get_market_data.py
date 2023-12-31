'''Gets Given Market Data from Binance API'''

import os 
from dotenv import load_dotenv
import ccxt
import pandas as pd

load_dotenv()

key = os.getenv('API_KEY_Binance')
secret = os.getenv('API_SECRET_Binance')

exchange1 = ccxt.binance({
    'apiKey': key,
    'secret': secret,
    'enableRateLimit': True,
})

symbol = 'ADA/USDT'
timeframe='15m'
limit = 500

bars = exchange1.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
print(df)





