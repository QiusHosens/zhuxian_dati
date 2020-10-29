# -*- coding: utf-8 -*

import requests
url = 'http://114.115.155.228:8089/api/tr-run/'
img1_file = {
    'file': open('./images/20201027204718373155.png', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)

raw_out = res.json().get('data').get('raw_out')

results = []
for raw in raw_out:
    print raw[1]
    results.append(raw[1])
print results[0]