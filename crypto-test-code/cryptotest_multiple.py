import json
from queue import Queue

from cryptoio import *
from Account import Account

symbols = ["btc", "eth", "ada"]
interval = "1m"
sockets = ["wss://stream.binance.com:9443/ws/{}usdt@kline_{}".format(symbol, interval) for symbol in symbols]

threads = []
queue = Queue()
account = Account(10000)
cont = True

def process_input(raw_input, account, threads, price_updater):
    prices = price_updater.prices
    args = raw_input.lower().split(" ")
    if args[0] == "balance":
        print(account.balance)
    if args[0] == "prices":
        print("Current prices: ")
        for key in prices.keys():
            print(key, prices[key])
    if args[0] == "buy":
        symb = (args[1] + "usdt").upper()
        amount = float(args[2])
        account.buy(symb, amount, prices[symb])
    if args[0] == "sell":
        pass
    if args[0] == "portfolio":
        print(json.dumps(account.portfolio, indent=2))
        print("Total worth: " + str(account.portfolio_value(price_updater.prices)))
    if args[0] == "exit":
        for t in threads:
            t.ws.close()
        price_updater.running = False
        return False
    return True


for socket in sockets:
    thread = WebSocketThread(queue, socket)
    threads.append(thread)

price_updater = PriceUpdater(queue)
price_updater.start()

for t in threads:
    t.start()

while cont:
    raw_input = input(" > ")
    cont = process_input(raw_input, account, threads, price_updater)