import websocket, json

SYMBOL = "ethusdt"
INTERVAL = "1m"
SOCKET = "wss://stream.binance.com:9443/ws/{}@kline_{}".format(SYMBOL, INTERVAL)

count = 1

def on_open(ws):
    print("Socket opened!")

def on_close(ws):
    print("Socket closed!")

def on_message(ws, message):
    json_message = json.loads(message)
    print(json_message["k"]["c"])

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()