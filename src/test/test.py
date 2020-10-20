# -*- coding: utf-8 -*

import requests
url = 'http://114.115.155.228:8089/api/tr-run/'
img1_file = {
    'file': open('./images/test_1.png', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)

raw_out = res.json().get('data').get('raw_out')

results = []
for raw in raw_out:
    results.append(raw[1])
print results

str = '\u600e\u6837\u7684\u96e8,\u600e\u6837\u7684\u591c,\u600e\u6837\u7684\u6211'
print str.decode('unicode-escape')