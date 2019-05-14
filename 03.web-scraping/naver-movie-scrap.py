import requests
from bs4 import BeautifulSoup
import pprint

# 1. html 긁어오기
res = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')

print(res.headers['Content-Length'])

# 파싱을 위한 soup객체 변환
soup = BeautifulSoup(res.text, 'html.parser')

# 타겟 태그 확보
tbody = soup.select_one('#old_content > table > tbody')
# tbody 밑에 모든 tr태그를 확보
trs = tbody.find_all('tr')

BASE_URL = 'http://movie.naver.com'

result = []
for item in trs:
    try:
        # 1. 제목 확보
        title = item.find_all('td')[1].find('div').find('a').text
        # 2. 순위 확보
        ranking = int(item.find_all('td')[0].find('img')['alt'])
        # 3. 영화상세 URL 확보
        url = item.find_all('td')[1].find('div').find('a')['href']

        result.append([ranking, title, BASE_URL + url])
    except:
        pass

pprint.pprint(result)
