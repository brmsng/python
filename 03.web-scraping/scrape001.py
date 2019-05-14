import requests
from bs4 import BeautifulSoup

# http client 를 이용 HTML을 확보
res = requests.get('https://nenechicken.com/17_new/sub_shop01.asp')

# 단순응답 텍스트(HTML)를 파싱할 수 있게 객체(parsable object)로 변환
soup = BeautifulSoup(res.text)
the_div = soup.select_one('#STORE > div > div > div > div.shopCover > div')

store_list = the_div.find_all('div', {'class': 'shop'})

print(len(store_list))



# #STORE > div > div > div > div.shopCover > div
# //*[@id="STORE"]/div/div/div/div[1]/div