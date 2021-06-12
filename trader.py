import time
from crypto import Crypto

class Trader:
    def __init__(self, crypto="BTCCAD", capital=20000, interval=5):
        self.balance = capital
        self.crypto_wallet = 0
        self.interval = interval
        self.buy_amount = 200 #How many dollars to buy when appropriate
        self.sell_amount = 200
        self.buy_threshold = 50
        self.sell_threshold = 50
        self.crypto = Crypto(crypto)
        self.history = []

    def trade(self):
        while(True):
            res = self.crypto.fetch()
            self.history.append({'ask':res['ask'], 'bid': res['bid']})
            print('==================')
            print('ask:', "${:.2f}".format(res['ask']))
            print('bid:', "${:.2f}".format(res['bid']))
            print('\n')
            ask_avg, bid_avg = self.calc_average(15)
            print('ask avg:', "${:.2f}".format(ask_avg))
            print('bid avg:', "${:.2f}".format(bid_avg))
            print('\n')
            print('balance:', "${:.2f}".format(self.balance))
            print('crypto wallet:', self.crypto_wallet)
            print('value:', "${:.2f}".format(self.balance + (self.crypto_wallet * ask_avg)))
            print('==================')

            if len(self.history) > 15:
                if res['ask'] > (ask_avg + self.buy_threshold) and self.balance > self.buy_amount:
                    self.balance -= self.buy_amount
                    bought = self.crypto.buy(self.buy_amount)
                    self.crypto_wallet += bought
                    print(f"\nBuying {bought} for ${self.buy_amount}")
                elif res['bid'] < (bid_avg - self.sell_threshold):
                    sold, amount = self.crypto.sell(self.sell_amount, self.crypto_wallet)
                    if sold:
                        self.crypto_wallet -= sold
                        self.balance += amount
                        print(f"\nSelling {sold} for ${amount}")

            time.sleep(self.interval)
            
    def calc_average(self, n):
        a = 0
        b = 0
        for h in self.history[-n:]:
            a += float(h['ask'])
            b += float(h['bid'])
        
        return a/len(self.history[-n:]), b/len(self.history[-n:])


    def check(self):
        pass

if __name__ == '__main__':
    tdr = Trader(interval=60)
    tdr.trade()