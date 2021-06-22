from collector import *
from ta.momentum import RSIIndicator

def main():
    collector = HistDataCollector(["btc"])
    collector.save_data()
    data_list = collector.load_data()

    # do stuff with data
    # probably (1) compute indicators; (2) train model
    df = data_list[0]
    r = RSIIndicator(df.iloc[:, 3], window=10)
    print(df.iloc[:, 3])
    print(r.rsi())

if __name__ == "__main__":
    main()