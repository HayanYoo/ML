import re
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url="https://news.naver.com")

elems = driver.find_elements_by_css_selector(".hdline_article_tit [href]")
links = [elem.get_attribute('href') for elem in elems]

for link in links:

    driver.get(link)

    title = re.sub('[/\"\?]', ' ', driver.find_element_by_id("articleTitle").text)
    d = driver.find_element_by_id("articleBodyContents")

    file = open(f"{title}.txt", "w", encoding='utf8')
    file.write(d.text)
    file.close()

