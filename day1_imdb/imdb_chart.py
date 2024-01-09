# Goal: imdb top 250 movies title

import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

area = soup.select("#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li")

if area:
    rank = 1
    for item in area:
        title = item.select_one("h3").text
        print(rank, ": ", title)
        rank += 1
else:
    print("The data could not be retrieved.")
