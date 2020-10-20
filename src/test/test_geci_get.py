# -*- coding: utf-8 -*

import bs4
import re
import requests
import lxml.html
import itertools

def del_adjacent(list, symbol):
    for i in range(len(list) - 1, 0, -1):
        if list[i] == symbol and list[i] == list[i-1]:
            del list[i]

if __name__=="__main__":
    file_path = './source/igeci_geci.txt'
    # 清空数据
    # geci_file = open(file_path, 'w')
    # geci_file.truncate()
    # geci_file.close()

    geci_url = 'http://www.igeci.cn/denglijun/15149.html'
    print geci_url
    geci_resp = requests.get(geci_url).content
    geci_resp_soup = bs4.BeautifulSoup(geci_resp, "lxml")
    geci_content = geci_resp_soup.find(class_ = 'lyric-content')
    # 将所有br换成逗号
    for br in geci_content.findAll('br'):
        br.insert(0, ',')
    geci_result = geci_content.text.replace('\n', '').replace('\r', '').replace(' ', '')
    geci_result_list = list(geci_result)
    # 相邻逗号去重
    del_adjacent(geci_result_list, ',')
    geci_result = "".join(geci_result_list)
    print geci_result

    geci_file = open(file_path, 'a')
    geci_file.write(geci_result.encode("utf-8") + '\n')
    geci_file.close()