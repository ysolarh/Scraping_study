from bs4 import BeautifulSoup
import requests

st = input("회차: ")
# url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={st}회로또당첨번호"
header_user = {"User-Agent": "Mozilla/5.0"}

req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html, "html.parser")

winning_div = soup.select(".winning_number > .ball")
bonus_div = soup.select_one(".bonus_number > .ball")

result = []
for i in winning_div:
    result.append(i.text)
result.append(bonus_div.text)
print(result)
