from lotto_selenium import *
from export import *

if __name__ == '__main__':
    st = input("회차: ")
    winning_nums = get_winning_nums(st)
    print(winning_nums)
    export_to_csv(st, winning_nums)