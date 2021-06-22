class Account:
    portfolio = {}

    def __init__(self, balance):
        self.balance = balance # in usdt
        
    def buy(self, token_name, amount, price):
        total_price = amount * price
        
        if self.balance >= total_price:
            if token_name in self.portfolio:
                self.portfolio[token_name] += amount
            else:
                self.portfolio[token_name] = amount
            self.balance -= total_price
        else:
            raise ValueError("Can't buy more than you have! Trying to buy {} worth of {} with a balance of {}".format(
                total_price, token_name, self.balance))

    def sell(self, token_name, amount, price):
        if token_name in self.portfolio:
            if self.portfolio[token_name] >= amount:
                self.portfolio -= amount
                self.balance += amount * price
            else:
                raise ValueError("Can't sell more than you have! Trying to sell {} {} with only {}".format(
                    amount, token_name, self.portfolio[token_name]))
        else:
            raise ValueError("Can't sell more than you have! Trying to sell {} {} when you have none!".format(
                amount, token_name))

    def portfolio_value(self, prices):
        sum = self.balance
        for key in self.portfolio.keys():
            sum += self.portfolio[key] * prices[key]
        return sum