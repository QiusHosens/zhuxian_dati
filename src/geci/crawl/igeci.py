# -*- coding: utf-8 -*

# http://www.igeci.cn/
# 先从http://www.igeci.cn/geshou/获取歌手链接,再在每个歌手链接后加 数字+.html 遍历歌词

import bs4
import re
import requests
import lxml.html
import time
from datetime import datetime

def get_a_url_list(soup, htmlClass):
    a_parents = soup.findAll(class_ = htmlClass)
    # print geshou_parent

    a_url_list = []
    for a_parent in a_parents:
        a_list = a_parent.findAll('a')
        for a in a_list:
            a_url_list.append(a.attrs['href'])
    return a_url_list

# dt = datetime.now()
# dtstr = dt.strftime('%Y%m%d%H%M%S%f')
# print dtstr
# file = open('../source/igeci_source_' + dtstr + '.txt','w') #,encoding='utf-8'

# 获取歌手链接
def get_geshou_url_list():
    geshou_all_url = 'http://www.igeci.cn/geshou/'
    geshou_all_resp = requests.get(geshou_all_url).content
    geshou_all_resp_soup = bs4.BeautifulSoup(geshou_all_resp, "lxml")

    # 歌手地址
    geshou_url_list = get_a_url_list(geshou_all_resp_soup, "lyric-star")
    return geshou_url_list

# 专辑地址
def get_zhuanji_url_list(geshou_url_list):
    zhuanji_url_list = []
    for geshou_url in geshou_url_list:
        geshou_resp = requests.get(geshou_url).content
        geshou_resp_soup = bs4.BeautifulSoup(geshou_resp, "lxml")
        geshou_zhuanji_url_list = get_a_url_list(geshou_resp_soup, "lyric-list")
        zhuanji_url_list += geshou_zhuanji_url_list
    return zhuanji_url_list

# 歌词地址
def get_and_save_geci_url_list(zhuanji_url_list, file_path, start, end):
    geci_url_list = []
    if end > len(zhuanji_url_list):
        end = len(zhuanji_url_list)
    # for zhuanji_url in zhuanji_url_list:
    for index in range(start, end):
        zhuanji_url = zhuanji_url_list[index]
        print zhuanji_url
        zhuanji_resp = requests.get(zhuanji_url).content
        zhuanji_resp_soup = bs4.BeautifulSoup(zhuanji_resp, "lxml")
        geshou_zhuanji_geci_url_list = get_a_url_list(zhuanji_resp_soup, "lyric-list")
        geci_url_list += geshou_zhuanji_geci_url_list

        geci_url_file = open(file_path,'a')
        for geci_url in geshou_zhuanji_geci_url_list:
            geci_url_file.write(geci_url.encode("utf-8") + '\n')
        geci_url_file.close()
        print index, geshou_zhuanji_geci_url_list
    print len(geci_url_list)

def del_adjacent(list, symbol):
    for i in range(len(list) - 1, 0, -1):
        if list[i] == symbol and list[i] == list[i-1]:
            del list[i]

# 获取歌词,每个br加个逗号
def get_and_save_geci_list(geci_url_list, file_path, start, end):
    if end > len(geci_url_list):
        end = len(geci_url_list)
    # for geci_url in geci_url_list:
    for index in range(start, end):
        geci_url = geci_url_list[index]
        # geci_url = 'http://www.igeci.cn/luhan/104108.html'
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
        print index, geci_result

        geci_file = open(file_path, 'a')
        geci_file.write(geci_result.encode("utf-8") + '\n')
        geci_file.close()

def save_geci_url_list(geci_url_file_path):
    # 清空数据
    # geci_url_file = open(geci_url_file_path,'w')
    # geci_url_file.truncate()
    # geci_url_file.close()

    # 获取歌手地址列表
    geshou_url_list = get_geshou_url_list()
    # 获取专辑地址列表
    zhuanji_url_list = get_zhuanji_url_list(geshou_url_list)
    # 获取并保存歌词地址列表
    get_and_save_geci_url_list(zhuanji_url_list, geci_url_file_path, 0, len(zhuanji_url_list))

if __name__=="__main__":
    # 歌词地址列表
    geci_url_file_path = '../source/igeci_geci_url.txt'
    # save_geci_url_list(geci_url_file_path)

    # 从文件读取歌词地址列表,只取中文,所以只读到104008行
    geci_url_file = open(geci_url_file_path)
    line = geci_url_file.readline()
    geci_url_list = []
    while line:
        print line
        geci_url_list.append(line.replace('\n', ''))
        line = geci_url_file.readline()
    geci_url_file.close()

    # 歌词列表
    geci_file_path = '../source/igeci_geci.txt'
    # 清空数据
    # geci_file = open(geci_file_path,'w')
    # geci_file.truncate()
    # geci_file.close()

    start = 95805
    end = 103966
    get_and_save_geci_list(geci_url_list, geci_file_path, start, end)