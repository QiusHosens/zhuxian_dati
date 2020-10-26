# -*- coding: utf-8 -*

from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(['114.115.155.228:29200'])

def upload_geci(id, geci):
    es.create(index="geci", doc_type="geci", id=id, body={"data": geci})

if __name__=="__main__":
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