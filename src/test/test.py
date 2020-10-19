# -*- coding: utf-8 -*

import requests
url = 'http://114.115.155.228:8089/api/tr-run/'
img1_file = {
    'file': open('./images/IMG_0220.PNG', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)

print res