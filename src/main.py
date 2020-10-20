# -*- coding: utf-8 -*

# test
import requests
url = 'http://192.168.31.108:8089/api/tr-run/'
img1_file = {
    'file': open('img1.png', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)