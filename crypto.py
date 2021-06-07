import requests

class Crypto:
    def __init__(self, crypto):
        self.crypto = crypto
        self.price = {'ask': 0, 'bid': 0}

    def fetch(self):
        resp = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={self.crypto}")
        data = resp.json()
        self.price['ask'] = float(data['result'][list(data['result'])[0]]['a'][0])
        self.price['bid'] = float(data['result'][list(data['result'])[0]]['b'][0])
        return self.price

    def buy(self, amount):
        return amount/self.price['ask']

    def sell(self, amount, wallet):
        selling = amount/self.price['bid']
        if selling <= wallet:
            return selling, amount
        elif wallet > 0:
            return wallet, wallet * self.price['bid']
        return 0, 0




if __name__ == '__main__':
    btc = Crypto('BTCCAD')
    btc.fetch()