# -*- coding: utf-8 -*-
import requests
import re
import MySQLdb
from lxml import etree


# 从itechzero网站上爬取谷歌镜像
def spider_from_itechzero():
    try:
        res = requests.get('http://www.itechzero.com/google-mirror-sites-collect.html')
        res.raise_for_status()
        url_set = pattern_url_by_xpath_from_itechzero(res.text.encode(res.encoding))
        add_to_database(url_set)
    except requests.exceptions.RequestException, e:
        print e


# 从自在饭网站上爬取谷歌镜像
def spider_from_zizaifan():
    try:
        res = requests.get('http://zizaifan.com/html/google.html')
        res.raise_for_status()
        url_set = pattern_url_by_xpath_from_zizaifan(res.text.encode(res.encoding))
        add_to_database(url_set)
    except requests.exceptions.RequestException, e:
        print e


# 使用xPath爬取谷歌镜像地址
def pattern_url_by_xpath_from_zizaifan(text):
    url_set = set()
    doc = etree.HTML(text)
    array = doc.xpath('//span[@class="tags cblue"]/following::*[1]/a/@href')
    for item in array:
        url_set.add(item)
    return url_set


# 将谷歌镜像地址存入数据库
def add_to_database(url_set):
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='google_spider')
    cur = conn.cursor()
    for item in url_set:
        count = cur.execute('SELECT id FROM googleUrl WHERE url="' + item + '"')
        if count > 0:
            cur.execute('UPDATE googleUrl SET updatetime = now(), isvalid = 1 WHERE url="' + item + '"')
        else:
            cur.execute('INSERT INTO googleUrl(url,updatetime,isvalid) VALUES("' + item + '", now(), 1)')
    cur.close()
    conn.commit()
    conn.close()


# 使用xPath爬取谷歌镜像地址
def pattern_url_by_xpath_from_itechzero(text):
    url_set = set()
    doc = etree.HTML(text)
    array = doc.xpath('//div[@class="entry-content"]/h3[2]/following::*[1]/span/following::*[1]/@href')
    for item in array:
        url_set.add(get_redirection_url(item))
    return url_set


# 正则表达式爬取谷歌镜像地址
def pattern_url_from_itechzero(text_array):
    url_set = set()
    for text in text_array:
        match = re.match(r'.*\[推荐\].*<a href="(.*)" target="_blank">.*', text)
        if match:
            url_set.add(get_redirection_url(match.group(1)))
    return url_set


# 获取重定向后的url地址
def get_redirection_url(url):
    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()
        return res.url
    except requests.exceptions.RequestException, e:
        return 'https://www.google.com'


if __name__ == '__main__':
    spider_from_itechzero()
    # spider_from_zizaifan()
