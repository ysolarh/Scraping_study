from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

st = input("회차: ")
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="

driver = webdriver.Chrome()
driver.get(url)

query_input = driver.find_element(By.ID, "nx_query")
query_input.send_keys(f"{st}회로또당첨번호")
query_input.send_keys(Keys.RETURN)

winning_div = driver.find_element(By.CLASS_NAME, "winning_number")
bonus_div = driver.find_element(By.CLASS_NAME, "bonus_number")
winning_nums = winning_div.find_elements(By.CLASS_NAME, "ball")
bonus_num = bonus_div.find_element(By.CLASS_NAME, "ball")

result = []
for i in winning_nums:
    result.append(i.text)
result.append(bonus_num.text)
print(result)
