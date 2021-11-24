import time

import chromedriver_autoinstaller
from selenium import webdriver


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url="https://news.naver.com")
a = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul')
b = driver.find_element_by_class_name("hdline_article_list")
c= b.find_elements_by_tag_name("a")
c[0].click()
d = driver.find_element_by_id("articleBodyContents")


file = open("aaa.txt", "w")
file.write(b.text)
file.close()

k= 1