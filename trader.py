import time
from crypto import Crypto

class Trader:
    def __init__(self, crypto="BTCCAD", capital=1000, interval=5):
        self.balance = capital
        self.interval = 60
        self.crypto = Crypto(crypto)
        self.history = []

    def trade(self):
        while(True):
            res = self.crypto.fetch()
            self.history.append({'ask':res['ask'], 'bid': res['bid']})
            print(res)
            self.calc_average(15)
            time.sleep(self.interval)
            
    def calc_average(self, n):
        a = 0
        b = 0
        print(self.history[-n:])
        for h in self.history[-n:]:
            a += float(h['ask'])
            b += float(h['bid'])
        
        print(a/len(self.history[-n:]), b/len(self.history[-n:]))


    def check(self):
        pass

if __name__ == '__main__':
    tdr = Trader()
    tdr.trade()