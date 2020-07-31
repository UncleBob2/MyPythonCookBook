'''Javascript Object Notation'''

import json

with open('JSON Country.json') as f:
    data = json.load(f)

for idex in data['country']:
    #print(idex['name'], idex['code'])
    del idex['code']

with open('JSON country_edit.json', 'w') as f:
    json.dump(data, f, indent=2)
