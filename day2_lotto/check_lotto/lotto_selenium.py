from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_html():
    global driver
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
    driver = webdriver.Chrome()
    driver.get(url)


def search(st):
    query_input = driver.find_element(By.ID, "nx_query")
    query_input.send_keys(f"{st}회로또당첨번호")
    query_input.send_keys(Keys.RETURN)


def extract_winning():
    winning_div = driver.find_element(By.CLASS_NAME, "winning_number")
    winning_div_child = winning_div.find_elements(By.CLASS_NAME, "ball")
    return winning_div_child


def extract_bonus():
    bonus_div = driver.find_element(By.CLASS_NAME, "bonus_number")
    bonus_div_child = bonus_div.find_element(By.CLASS_NAME, "ball")
    return bonus_div_child


def combine_winning_bonus():
    result = []
    all_winnings = extract_winning()
    for i in all_winnings:
        result.append(i.text)
    result.append(extract_bonus().text)
    return result


def extract_draw_date():
    date_a = driver.find_element(By.CSS_SELECTOR, ".text._select_trigger._text")
    date = date_a.text.replace(')', '(')
    date = date.split('(')[1]
    return date


def extract_prize_money():
    prize_p = driver.find_element(By.CLASS_NAME, "win_text")
    prize_p_child = prize_p.find_element(By.CLASS_NAME, "emphasis")
    return prize_p_child.text


def get_winning_nums(st):
    get_html()
    search(st)
    data = combine_winning_bonus()
    data.insert(0, st)
    data.insert(1, extract_draw_date())
    data.insert(2, extract_prize_money())
    return data
