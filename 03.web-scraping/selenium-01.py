from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

driver.implicitly_wait(3)
# 헤더에 User-Agent 변경

driver.get('http://www.wemakeprice.com/main/100020')
# res = requests.get('http://www.naver.com')
time.sleep(3)
driver.get('http://www.daum.net')
time.sleep(3)
html = driver.page_source
driver.close()

print(html)
