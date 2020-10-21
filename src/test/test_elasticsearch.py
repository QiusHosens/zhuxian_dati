# -*- coding: utf-8 -*

from elasticsearch import Elasticsearch

es = Elasticsearch(['114.115.155.228:9200'])
# es.create(index="geci", doc_type="geci", id=11, ignore=[400,409], body={"data":'歌词来源专辑：华语女歌手/邓丽君/甜蜜蜜阵阵春风柔-邓丽君,又是一年芳草遍地,阵阵春风柔,也正是我和你离别的时候,青山不改绿水长流,我俩要把这句誓言,牢牢记心头,只等到再相聚首,只等到我俩再相聚首,又一年春风柔,又是一年花开似锦,阵阵春风柔,也正是我和你相逢的时候,青山不改绿水长流,请信我俩把这誓言,依然记心头,到今天又相聚首,到今天我俩又相聚首,又一年春风柔'})
query = es.search(index="geci", body={"query":{"wildcard" : { "data" : "*阵阵春风柔*" }}})
print query