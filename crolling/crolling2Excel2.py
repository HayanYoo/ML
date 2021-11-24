#검색 크롤링
# 1. 패키지 install

import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

# 1. 검색어 입력하기
search = input("검색할 데이터를 입력해주세요 : ")
# 2. 데이터 크롤링 진행하기
sheet.append(["검색어명", "기사 제목", "기사 요약"])

for p in range(1, 10+1, 1):
    raw = requests.get("https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&cluster=y&q={s}&p={p}".format(s = search, p = p))
    html = BeautifulSoup(raw.text, 'html.parser')

    container = html.select("ul.list_news li")

    for c in container:
        # 기사 제목 : div.wrap_tit.mg_tit a
        title = c.select_one("div.wrap_cont a").text.strip()
        # 기사 요약 : p.f_eb.desc
        content = c.select_one("div.wrap_cont p").text.strip()

        sheet.append([search, title, content])

wb.save("daum_news.xlsx")
