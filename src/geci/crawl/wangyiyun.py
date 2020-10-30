# -*- coding: utf-8 -*
# 改地址为用户歌单,暂不爬取
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
driver = webdriver.Chrome('../../driver/win32/chromedriver.exe',
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
    href_prefix = "https://music.163.com/#"
    offset = 105
    zhuanji_page_url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset=105"
    driver.get(zhuanji_page_url)
    zhuanji_iframes = driver.find_elements_by_tag_name('iframe')
    # print iframes
    zhuanji_iframe = zhuanji_iframes[0]
    driver.switch_to.frame(zhuanji_iframe) # 最重要的一步
    zhuanji_page_resp_soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

    # zhuanji_page_resp_soup = getDriverHttp(zhuanji_page_url)
    zhuanji_page_hrefs = get_zhuanji_url_list(zhuanji_page_resp_soup, 'm-pl-container')
    print zhuanji_page_hrefs

    for zhuanji_href in zhuanji_page_hrefs:
        driver.get(zhuanji_href)
        ge_page_frame = driver.find_elements_by_tag_name('iframe')[0]
        driver.switch_to.frame(ge_page_frame)
        ge_page_resp_soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

        # TODO