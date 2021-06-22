from binance import Client
import pandas as pd

class HistDataCollector:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        api_key, secret_key = self.load_keys() # put api key in first line, secret key in 2nd line of keys.txt
        self.client = Client(api_key, secret_key)
        
    def save_data(self):
        for t in self.tokens:
            pair = (t + "usdt").upper()
            f = open("data/{}.csv".format(t), "w+")
            data = self.client.get_historical_klines(pair, Client.KLINE_INTERVAL_1WEEK, start_str=0)
            for x in data:
                n = 6
                for i in range(1, n):
                    f.write(str(x[i]))
                    if i < n - 1: f.write(",")
                f.write("\n")
            f.close()

    def load_data(self):
        df_list = []
        for t in self.tokens:
            df = pd.read_csv("data/{}.csv".format(t))
            df_list.append(df)
        return df_list

    def load_keys(self):
        f = open("keys.txt", "r")
        api_key = f.readline().strip()
        secret_key = f.readline().strip()
        f.close()
        return api_key, secret_key