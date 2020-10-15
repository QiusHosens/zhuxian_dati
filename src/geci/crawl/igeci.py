# -*- coding: utf-8 -*

# http://www.igeci.cn/
# 先从http://www.igeci.cn/geshou/获取歌手链接,再在每个歌手链接后加 数字+.html 遍历歌词

import bs4
import re
import requests
import lxml.html
import time

print time.localtime()
# file = open('../source/igeci_source_' +  + '.txt','w')#,encoding='utf-8'
#file.truncate()