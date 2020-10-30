# -*- coding: utf-8 -*

from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(['114.115.155.228:29200'])

def upload_geci(id, geci):
    es.create(index="geci", doc_type="geci", id=id, body={"data": geci})

def update_file_all():
    geci_file_path = '../geci/source/igeci_geci.txt'

    geci_file = open(geci_file_path)
    line = geci_file.readline()
    index = 0
    dt = datetime.now()
    dtstr = dt.strftime('%Y%m%d%H%M%S%f')
    while line:
        print (line)
        line = line.replace('\n', '')
        upload_geci(dtstr + str(index), line)
        index += 1
        line = geci_file.readline()
    geci_file.close()

if __name__=="__main__":
    # update_file_all();
    index = 0
    dt = datetime.now()
    dtstr = dt.strftime('%Y%m%d%H%M%S%f')
    line = '今天晚上当我醒来的时候,我的脚指头在蠢蠢欲动,它说今天晚上心情很不错,想到街上走走,,于是暗暗的天空开始灯光闪烁,世界变得有一点无厘头,我的心情像土拨鼠在挖洞,想找到出口,找到出口,,谁负责轰隆隆的节奏,快出来自首,一起到遥远的外太空,去甩一甩头,我今天决定我要放纵,我要high过头,我要到所有人的梦中和世界牵手,牵手,牵手,奇怪的废话少说,牵手,牵手,我的热情全年无休,牵手,牵手,烦人的步骤先跳过,牵手,牵手,我随时随地有空,牵手,牵手,奇怪的废话少说,牵手,牵手,我的热情全年无休,牵手,牵手,烦人的步骤先跳过,牵手,牵手,我随时随地有空,,谁负责轰隆隆的节奏,快出来自首,一起到遥远的外太空去甩一甩头,我今天决定我要放纵我要high过头,我要到所有人的梦中和世界牵手,,和世界牵手,牵手,牵手,奇怪的废话少说,牵手,牵手,我的热情全年无休,牵手,牵手,烦人的步骤先跳过,牵手,牵手,我要今夜刮起台风'

    upload_geci(dtstr + str(index), line)