import json
from urllib.request import urlopen

with urlopen('https://api.exchangeratesapi.io/latest') as response:
    source = response.read()

data = json.loads(source)
# print(json.dumps(data, indent=2))

usd_rates = dict()  # create new dic from JSON for quicker access

# for item in data['list']['resources']:
#     name = item['resources']['field']['name']
#     price = item['resources']['field']['price']
#     usd_rates[name] = price

for item in data['rates']:
    # print(item, end='  ')
    # print(data['rates'].get(item))
    usd_rates[item] = data['rates'].get(item)

print('The rate of CAD vs EUR', usd_rates['CAD'])
print('50 EUR in $CAD = ', 50 * float(usd_rates['CAD']))
