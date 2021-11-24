from urllib.request import urlretrieve

import chromedriver_autoinstaller
from selenium import webdriver
# curl 사용 가능

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get(url="https://www.gov.kr/")

a = driver.find_element_by_class_name("right-element")
b = a.find_elements_by_tag_name("a")
b[0].click()

a2 = driver.find_element_by_class_name("tab-element")
b2 = a2.find_elements_by_tag_name("a")
b2[4].click()

a3 = driver.find_element_by_class_name("nonMember_wrap")
b3 = a3.find_elements_by_tag_name("a")
b3[0].click()

images = driver.find_elements_by_css_selector(".cs-confirm-num > p > img")
img_url = images[0].get_attribute('src')
urlretrieve(img_url, '../opencv/captcha/src/captcha.jpg')
