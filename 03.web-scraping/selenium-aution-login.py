from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

opts = Options()
opts.add_argument('headless')
opts.add_argument('window-size=1920x1080')
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36")

driver = webdriver.Chrome('./chromedriver', chrome_options=opts)
driver.implicitly_wait(3)
print('driver ready..')

driver.get('https://memberssl.auction.co.kr/Authenticate/')
print('로그인화면 이동')
driver.find_element_by_id('id').send_keys('luxclinic')
driver.find_element_by_id('password').send_keys('1q2w3e4r%%')
time.sleep(1)
driver.find_element_by_id('Image1').click()
print('로그인 완료')
time.sleep(3)

driver.get('http://reward.auction.co.kr/MyPoint/SmilePointList.aspx')
print('마이포인트 화면 이동')
time.sleep(1)
html = driver.page_source
driver.close()
print('driver killed..')

# 스크래핑 대상 html 확보..
soup = BeautifulSoup(html, 'lxml')

print(soup)