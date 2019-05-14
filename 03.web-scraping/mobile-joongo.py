import requests
from bs4 import BeautifulSoup

# 헤더세팅
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# body(Form-data) 세팅
data = {
    'search.clubid': '10050146',
    'search.menuid': '1540',
    'search.boardtype': 'L',
    'search.questionTab': 'A',
    'search.totalCount': '201',
    'search.page': 7,
}

res = requests.post('https://m.cafe.naver.com/ArticleListAjax.nhn', headers=headers, data=data)

soup = BeautifulSoup(res.text, 'lxml')

li_tags = soup.find('ul', {'class': 'list_area'}).find_all('li', recursive=False)

result = []
for li in li_tags:
    title = li.find('a', {'class': 'txt_area'})\
                .find('strong')\
                .text.strip()
    id = li.find('a', {'class': 'txt_area'})\
                .find('div')\
                .find('span', {'class': 'ellip'})\
                .text
    write_date = li.find('a', {'class': 'txt_area'})\
                .find('div')\
                .find('span', {'class': 'time'})\
                .text
    result.append([title, id, write_date])

print(result)


