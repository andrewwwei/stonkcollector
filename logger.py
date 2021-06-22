import datetime

class Logger:
    def __init__(self, filename, dir="."):
        self.dir = dir
        self.filename = filename
        self.open_file(filename)

    def log(self, msg):
        current_time = str(datetime.datetime.now()).split(".")[0]
        self.file.write("[{}] {}\n".format(current_time, msg))

    def open_file(self, filename):
        self.file = open("{}/{}.log".format(self.dir, filename), "a+")

    def new_file(self, filename):
        self.close()
        self.open_file(filename)

    def close(self):
        self.file.close()

class TransactionLogger(Logger):
    def __init__(self):
        super().__init__(self.current_date(), dir="logs")

    def log_buy(self, token, price, amt):
        self.update_file()
        self.log("Bought {} {} at ${}, total ${}".format(amt, token, price, amt * price))

    def log_sell(self, token, price, amt):
        self.update_file()
        self.log("Sold {} {} at ${}, total ${}".format(amt, token, price, amt * price))

    def update_file(self):
        if not self.filename == self.current_date():
            self.new_file(self.current_date())

    def close(self):
        # do something
        super().close()

    def current_date(self):
        return str(datetime.datetime.now()).split(" ")[0]