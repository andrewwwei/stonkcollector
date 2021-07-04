from collector import *
from data_processing import *
from ta.momentum import RSIIndicator

def main():
    collector = HistDataCollector(["btc"])
    collector.save_data()
    data_list = collector.load_data()

    # do stuff with data
    # probably (1) compute indicators; (2) train model
    df = data_list[0]
    print(rsi(df))

if __name__ == "__main__":
    main()