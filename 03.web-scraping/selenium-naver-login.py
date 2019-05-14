from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36")

driver = webdriver.Chrome('./chromedriver', chrome_options=opts)
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_id('id').send_keys('ssgoni')
driver.find_element_by_id('pw').send_keys('')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(5)

driver.close()