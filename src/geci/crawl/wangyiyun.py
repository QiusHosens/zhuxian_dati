# -*- coding: utf-8 -*
# https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset=105

import bs4
import re
import requests
import lxml.html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from pyvirtualdisplay import Display

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('/usr/local/Sunanang/chromedriver/chromedriver',
                          chrome_options=chrome_options)

def getDriverHttp(url):
    driver.get(url)
    iframe = driver.find_elements_by_tag_name('iframe')[1]
    driver.switch_to.frame(iframe) # 最重要的一步
    soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
    return soup


# def getVideoUrl(url):
#     soup = getHttp(url)
#     miPlayer = soup.find('div', id='J_miPlayer')
#     url = miPlayer.find('video').get('src')
#     driver.quit()
#     return url

def get_zhuanji_url_list(soup, htmlClass):
    ul = soup.find(id = htmlClass)
    li_list = ul.findAll('li')
    hrefs = []
    for li in li_list:
        dec = li.find(class_ = 'dec')
        a = dec.find('a')
        hrefs.append(a.attrs['href'])
    return hrefs

if __name__=="__main__":
    offset = 105
    zhuanji_page_url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset=105"
    zhuanji_page_resp_soup = getDriverHttp(zhuanji_page_url)
    hrefs = get_zhuanji_url_list(zhuanji_page_resp_soup, 'm-pl-container')
    print hrefs

