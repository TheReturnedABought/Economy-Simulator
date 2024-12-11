class Person:
    def __init__(self, id, money=0, stocks=0):
        self.id = id
        self.money = money
        self.stocks = stocks

    def __str__(self):
        return f"Person {self.id}: Money=${self.money}, Stocks={self.stocks}"

    def produce_value(self):
        return self.money + 210