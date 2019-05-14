import os
import sys
import urllib.request
import json
import pprint

client_id = "VLJn8VU0yBV4yf18zXbs"
client_secret = "NrPWgrRf5y"
encText = urllib.parse.quote("서울시 서대문구 창천동 72-36")
url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()


if(rescode==200):
    response_body = response.read().decode('utf-8')
else:
    print("Error Code:" + rescode)

# print(response_body)
jTxt = json.loads(response_body)

print(jTxt['result']['items'])

for h in jTxt['result']['items']:
    print(h['point']['x'])
    print(h['point']['y'])
