from ta.volume import *
from ta.trend import *
from ta.momentum import *

def rsi(df):
    r = RSIIndicator(df.iloc[:, 4], window=10)
    return r.rsi()

def obv(df):
    o = OnBalanceVolumeIndicator(df.iloc[:, 5], df.iloc[:, 6])
    return o.on_balance_volume()

def adl(df):
    a = AccDistIndexIndicator(df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], df.iloc[:, 6])
    return a.acc_dist_index()

def adx(df):
    a = ADXIndicator(df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5])
    return a.adx()

def output_labels(df):
    r = rsi(df)
    labels = []
    prices = df.iloc[:, 1]
    mult = 1.002
    shift = 5
    
    # generate labels for data
    for i in range(10, len(r) - shift):
        # trash criteria
        if r[i] < 20 and prices[i + shift] > mult * prices[i]:
            labels.append(1)
        else:
            labels.append(0)
    return labels
