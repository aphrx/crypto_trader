import requests

class Crypto:
    def __init__(self, crypto):
        self.crypto = crypto
        self.price = {'ask': 0, 'bid': 0}

    def fetch(self):
        resp = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={self.crypto}")
        data = resp.json()
        self.price['ask'] = data['result'][list(data['result'])[0]]['a'][0]
        self.price['bid'] = data['result'][list(data['result'])[0]]['b'][0]
        return self.price

if __name__ == '__main__':
    btc = Crypto('BTCCAD')
    btc.fetch()