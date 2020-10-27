# -*- coding: utf-8 -*

# 1、截图题目部分
# 2、识别题目
# 3、搜索歌词库
# 4、搜索成功则输入到对应位置;搜索失败则保存到not_find.txt文件
from elasticsearch import Elasticsearch
import requests
from datetime import datetime
# from PIL import ImageGrab, Image

url = 'http://114.115.155.228:8089/api/tr-run/'
es = Elasticsearch(['114.115.155.228:29200'])
not_find_file = "not_find.txt"
delimiter = ","

image_path = "./images/"
left, bottom = 0, 268
# width, height = 1930, 1200
width, height = 574, 48
bbox = (left, bottom, left + width, bottom + height)

def ocr(image_addr):
    img1_file = {
        'file': open(file_addr, 'rb')
    }
    res = requests.post(url=url, data={'compress': 0}, files=img1_file)

    raw_out = res.json().get('data').get('raw_out')
    # raw_out数据:[[[227.49996948242188,22.999996185302734,448.99993896484375,33.428565979003906],"怎样的雨,怎样的夜,怎样的我",0.9950883947312832],[[548.2106323242188,22.050764083862305,23.2367000579834,29.59004783630371,4.0856170654296875],"?",0.999782383441925]]
    # 识别结果数组,意义:[[中心点x,中心点y,宽度,高度,旋转角度],中文结果,]
    # 先将换行的数据整合到一行,根据中心点y的位置判断是否为一行,整合到一行的时候同时修改中心点x的位置
    raw_center_y = raw_out[0][0][1]
    raw_height = raw_out[0][0][3]
    for raw in raw_out:
        # 如果中心点位置大于上一个位置的高度,则已换行;此时只改变中心点位置,加上图片宽度
        if raw[0][1] > raw_height:
            raw[0][0] += width

    # 计算填空位置
    empty_pos = 0
    diff_width = 50 # 水平距离大于50则认为是空处,这里为108
    index = 0
    for raw in raw_out:
        pos_curr = raw[0]
        x_start_curr = pos_curr[0] - pos_curr[2] / 2
        x_end_curr = pos_curr[0] + pos_curr[2] / 2

        has_next = index < len(raw_out)
        if has_next:
            pos_next = raw_out[index + 1][0]
            x_start_next = pos_next[0] - pos_next[2] / 2
            x_end_next = pos_next[0] + pos_next[2] / 2
        # 如果开始位置与图片0点相差规定宽度,则认为开始之前为填空位置
        if x_start_curr > diff_width:
            empty_pos = index
            break
        # 如果有下一个数据;如果结束位置与下一个位置相差规定宽度,则认为位置在本次到下次
        if has_next:
            if x_start_next - x_end_curr > diff_width:
                empty_pos = index + 1
                break
        else:
            empty_pos = index + 1
        index += 1
    # 目前存在下面几种情况:1、?a;2、a?;3、a?b
    results = []
    for raw in raw_out:
        results.append(raw[1])
    # print results[0]
    return empty_pos, results

def search(keys):
    # query = es.search(index="geci", doc_type="geci", body={"query": {"wildcard": {"data.keyword": condition}}})
    # query = es.search(index="geci", doc_type="geci", body={"query": {"match_phrase": {"data": {"query": condition}}}})
    must = []
    for key in keys:
        must.append({"match_phrase": {"data": {"query": key}}})
    query = es.search(index="geci", doc_type="geci", body={"query": {"bool": {"must": must}}})
    return query['hits']['hits']

if __name__=="__main__":
    # 每隔5s执行一次,执行
    dt = datetime.now()
    dtstr = dt.strftime('%Y%m%d%H%M%S%f')
    # file_addr = image_path + dtstr + '.png'
    file_addr = './images/test_1.png'
    # 截图 TODO
    # 识别题目
    empty_pos, titles = ocr(file_addr)
    # 搜索歌词
    # 去掉最后一个条件
    titles.pop()
    condition = ""
    index = 0
    for key in titles:
        if empty_pos == index:
            condition += "_"
        condition += key
        index += 1
    if empty_pos == index:
        condition += "_"
    print condition
    gecis = search(titles)
    # 未搜索到结果则写入未发现文件
    if len(gecis) == 0:
        geci_url_file = open(not_find_file,'a')
        geci_url_file.write(condition.encode("utf-8") + '\n')
        geci_url_file.close()
    # 搜索到则打印出来
    else:
        # print gecis
        # hits = gecis['hits']['hits']
        index = 0
        for hit in gecis:
            # print index, hit['_source']['data']
            index += 1
        # 有匹配则取第一条数据
        geci = gecis[0]['_source']['data']

        # 如果在0位置,则向上找到前一个逗号,到现在位置;如果是最后一个位置,则向下找到下一个逗号,从最后位置到逗号位置
        symbol = ","
        target = ""
        # 找出当前填空位置所在歌词位置,分为三种情况:1、?a;2、a?b;3、a?
        title_len = len(titles)
        if empty_pos == 0:
            first_index = geci.index(titles[empty_pos])
            prefix = geci[0:first_index]
            target = prefix[prefix.rfind(symbol):]
        elif empty_pos >= title_len:
            last_index = geci.index(titles[title_len - 1])
            suffix = geci[last_index + len(titles[title_len - 1]):]
            target = suffix[0:suffix.find(symbol)]
        else:
            prefix_index = geci.index(titles[empty_pos - 1])
            curr_index = geci.index(titles[empty_pos])
            target = geci[prefix_index + len(titles[empty_pos - 1]):curr_index]
        print target
        # TODO 直接写入相应位置