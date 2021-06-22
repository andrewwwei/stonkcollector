from ta.momentum import RSIIndicator

def getRSI(df):
    r = RSIIndicator(df.iloc[:, 3], window=10)
    print(df.iloc[:, 3])
    return r.rsi()