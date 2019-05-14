#! /usr/bin/python3
#-*- coding:utf-8 -*-

from lxml import html
import requests
import pprint
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


APIKEY = 'VLJn8VU0yBV4yf18zXbs'
client_sc = 'NrPWgrRf5y'
# MAPAPI = 'http://openapi.map.naver.com/api/geocode.php?key=%s&encoding=utf-8&coord=LatLng&query=%s'
MAPAPI = 'https://openapi.naver.com/v1/map/geocode?query='

# 예제 함수 not working for any reason...
# def get_latlon(query):
#     root = html.parse(MAPAPI % (APIKEY, query))
#     print(root.xpath)
#     lon, lat = root.xpath('//point/x/text()')[0], root.xpath('//point/y/text()')[0]
#     lon = root.xpath('//items/item')
#     lat = root.xpath('//point/y/text()')[0]
#     print(lon)
#     return(lat, lon)


def get_latlon(query):
    encText = urllib.parse.quote(query)
    request = urllib.request.Request(MAPAPI+encText)
    request.add_header("X-Naver-Client-Id", APIKEY)
    request.add_header("X-Naver-Client-Secret", client_sc)
    res = urllib.request.urlopen(request)
    rescode = res.getcode()

    if(rescode==200):
        res_body = res.read().decode('utf-8')
        res_body = BeautifulSoup(res_body, "lxml")
        # print(res_body.find("x").get_text())
        # x1 = [float(xy.get_text()) for xy in res_body.find_all("x")]
        # y1 = [float(xy.get_text()) for xy in res_body.find_all("y")]
        # print(x1, y1)
    else:
        print("Error code : "+ rescode)

    # return(x1, y1)


def prep(item):
    n, name = item[0].split(' ', 1)
    lat, lon = get_latlon(item[3])
    print(item[3])
    return{
        'num': n, 'name': name,
        'lat': lat, 'lon': lon,
        'description': item[1],
        'phone': item[2],
        'addr': item[3]
    }


# get data from article
r = requests.get('http://m.wikitree.co.kr/main/news_view.php?id=217101')
root = html.document_fromstring(r.text)
string = '\n'.join(root.xpath('//div[@id="descs"]/div//text()'))

items = []
for i in range(1, 21):
    tmp = string.split('%s.' % i, 1)
    string = tmp[1]
    items.append([j.strip() for j in tmp[0].split('\n') if j and j != '\xa0'])

# pprint.pprint(items)
data = [prep(i[:4]) for i in items[1:]]

#
# #save data to file
# with open('places.csv', 'w') as f:
#     f.write('name, lat, lon \n')
#     for d in data:
#         f.write('%(name)s, %(lat)s, %(lon)s\n' % d)