from ta.volume import *
from ta.trend import *
from ta.momentum import *

def rsi(df):
    r = RSIIndicator(df.iloc[:, 3], window=10)
    print(df.iloc[:, 3])
    return r.rsi()

def obv(df):
    o = OnBalanceVolumeIndicator(df.iloc[:, 4], df.iloc[:, 5])
    return o.on_balance_volume()

def adl(df):
    a = AccDistIndexIndicator(df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5])
    return a.acc_dist_index()

def adx(df):
    a = ADXIndicator(df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4])
    return a.adx()