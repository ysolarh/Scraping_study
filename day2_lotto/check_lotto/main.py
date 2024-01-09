from lotto_selenium import *
from export import *
from compare import *

if __name__ == '__main__':
    st = input("회차: ")
    winning_nums = get_winning_nums(st)
    export_to_csv(st, winning_nums)
    compare_nums(st)
