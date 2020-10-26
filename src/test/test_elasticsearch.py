# -*- coding: utf-8 -*

from elasticsearch import Elasticsearch

es = Elasticsearch(['114.115.155.228:29200'])

# 新增数据
# es.create(index="geci", doc_type="geci", id=12, ignore=[400,409], body={"data": "test123"})
# es.create(index="geci", doc_type="geci", id=11, ignore=[400,409], body={"data":'歌词来源专辑：华语女歌手/邓丽君/甜蜜蜜阵阵春风柔-邓丽君,又是一年芳草遍地,阵阵春风柔,也正是我和你离别的时候,青山不改绿水长流,我俩要把这句誓言,牢牢记心头,只等到再相聚首,只等到我俩再相聚首,又一年春风柔,又是一年花开似锦,阵阵春风柔,也正是我和你相逢的时候,青山不改绿水长流,请信我俩把这誓言,依然记心头,到今天又相聚首,到今天我俩又相聚首,又一年春风柔'})

# 删除数据
# es.delete(index="geci", doc_type="geci", id=12)
# es.delete(index="geci", doc_type="geci", id=11)

# 查询数据
query = es.search(index="geci", doc_type="geci", body={"query": {"wildcard": {"data.keyword": "*当誓言划向蓝色海岸线*"}}})
# query = es.search(index="geci", size=2)
# print query['hits']['hits'][0]['_source']['data']
# print query
hits = query['hits']['hits']
index = 0
for hit in hits:
    print index, hit['_source']['data']
    index += 1