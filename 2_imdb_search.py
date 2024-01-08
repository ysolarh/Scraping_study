# Goal: search movies

import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0"}

keyword = input("type the keyword: ")
url = f"https://www.imdb.com/find/?q={keyword}&ref_=nv_sr_sm"

req = requests.get(url, headers=header_user)
soup = BeautifulSoup(req.text, "html.parser")
area = soup.select(".ipc-metadata-list-summary-item__tc")
section = soup.select_one(".ipc-title__text").text


def get_movie_info(cnt, item):
    try:
        title = item.select_one(".ipc-metadata-list-summary-item__t").text
        release = item.select_one("ul:nth-of-type(1) > .ipc-inline-list__item").text
        actors = item.select_one("ul:nth-of-type(2) > .ipc-inline-list__item").text
#        actors = item.select_one("ul:nth-of-type(2) > li").text
        print(cnt, "\ntitle: ", title, "\nrelease: ", release, "\nactors: ", actors, "\n")
    except:
        print("Some info is missing in", cnt)


if area and section == "Titles":
    print('\nSearch: \"', keyword, '\"')
    cnt = 1
    for item in area[:5]:
        get_movie_info(cnt, item)
        cnt += 1
else:
    print("No information found")
