# -*- coding: utf-8 -*

# 1、截图题目部分
# 2、识别题目
# 3、搜索歌词库
# 4、搜索成功则输入到对应位置;搜索失败则保存到not_find.txt文件
from elasticsearch import Elasticsearch
import requests
from datetime import datetime

url = 'http://114.115.155.228:8089/api/tr-run/'
es = Elasticsearch(['114.115.155.228:29200'])
not_find_file = "not_find.txt"

def ocr(image_addr):
    img1_file = {
        'file': open(file_addr, 'rb')
    }
    res = requests.post(url=url, data={'compress': 0}, files=img1_file)

    raw_out = res.json().get('data').get('raw_out')

    results = []
    for raw in raw_out:
        results.append(raw[1])
    # print results[0]
    return results

def search(condition):
    query = es.search(index="geci", doc_type="geci", body={"query": {"wildcard": {"data.keyword": condition}}})
    return query['hits']['hits']

if __name__=="__main__":
    # 每隔5s执行一次,执行
    dt = datetime.now()
    dtstr = dt.strftime('%Y%m%d%H%M%S%f')
    file_addr = './images/' + dtstr + '.png'
    # 截图 TODO
    # 识别题目
    titles = ocr(file_addr)
    # 搜索歌词
    condition = "*"
    for key in titles:
        condition += key + "*"
    gecis = search(condition)
    # 未搜索到结果则写入未发现文件
    if len(gecis) == 0:
        geci_url_file = open(not_find_file,'a')
        geci_url_file.write(condition.encode("utf-8") + '\n')
        geci_url_file.close()
    # 搜索到则打印出来
    else:
        print gecis
        # TODO 直接写入相应位置