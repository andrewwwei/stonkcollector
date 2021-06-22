import threading, websocket, json
from queue import Queue

class WebSocketThread(threading.Thread):
    def __init__(self, queue, socket):
        threading.Thread.__init__(self)
        self.queue = queue
        self.ws = websocket.WebSocketApp(socket, on_message=self.on_message)

    def run(self):
        self.ws.run_forever()

    def on_message(self, ws, message):
        self.queue.put(message)

class PriceUpdater(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.prices = {}
        self.running = True

    def update_prices(self, queue):
        if not queue.empty():
            json_message = queue.get()
            message = json.loads(json_message)
            
            symb = message["k"]["s"]
            price = float(message["k"]["c"])
            self.prices[symb] = price

    def run(self):
        while self.running:
            self.update_prices(self.queue)
                