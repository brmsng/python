from lxml import html
import requests
import pprint
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd



addr=[]

# get data from article
r = requests.get('http://m.wikitree.co.kr/main/news_view.php?id=217101')
root = html.document_fromstring(r.text)
string = '\n'.join(root.xpath('//div[@id="descs"]/div//text()'))

items = []
for i in range(1, 21):
    tmp = string.split('%s.' % i, 1)
    string = tmp[1]
    items.append([j.strip() for j in tmp[0].split('\n') if j and j != '\xa0'])


for j in range(1, len(items)):
    a = items[j][3]
    n = items[j][0].split(' ', 1)[1]
    addr.append([n, a])

addr = pd.DataFrame(addr)

#Python에서 주소좌표변환 api를 호출
client_id = "VLJn8VU0yBV4yf18zXbs"
client_secret = "NrPWgrRf5y"

#변수 초기화
x=[]
y=[]
add=[]

# %%time
for k in addr[1]:
    try:
        encText = urllib.parse.quote(k)
        # url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
        url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText  # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        response_body = response.read().decode('utf-8')
        # response.close()
        response_body = BeautifulSoup(response_body, "lxml")
        pprint.pprint(response_body)
        x1 = [float(xy.get_text()) for xy in response_body.find_all("x")]
        y1 = [float(xy.get_text()) for xy in response_body.find_all("y")]
        # x.append(x1[0])
        # y.append(y1[0])
        # add.append(k)

    except:
        x.append(0)
        y.append(0)
        add.append(k)

addlatlong = pd.DataFrame({'NAME': addr[0], 'ADDR': add, 'Latitude': y, 'Longtitude': x})
addlatlong.to_csv("gourmet.csv", index=False)


