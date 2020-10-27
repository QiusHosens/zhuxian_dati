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
    line = '下雨天了怎么办,我好想你,不敢打给你,我找不到原因,为什么失眠的声音,变得好熟悉,沉默的场景,做你的代替,陪我等雨停,期待让人越来越沉溺,谁和我一样,等不到他的谁,爱上你我总在学会,寂寞的滋味,一个人撑伞,一个人擦泪,一个人好累,怎样的雨,怎样的夜,怎样的我能让你更想念,雨要多大,天要多黑,才能够有你的体贴,其实,没有我你分不清那些,差别,结局还能多明显,别说你会难过,别说你想改变,被爱的人不用道歉,期待让人越来越疲惫,谁和我一样,等不到他的谁,爱上你我总在学会,寂寞的滋味,一个人撑伞,一个人擦泪,一个人好累,怎样的雨,怎样的夜,怎样的我能让你更想念,雨要多大,天要多黑,才能够有你的体贴,其实,没有我你分不清那些,差别,结局还能多明显,别说你会难过,别说你想改变,被爱的人不用道歉,怎样的雨,怎样的夜,怎样的我能让你更想念,雨要多大,天要多黑,才能够有你的体贴,其实,没有我你分不清那些,差别,结局还能多明显,别说你会难过,别说你想改变,被爱的人不用道歉'
    upload_geci(dtstr + str(index), line)