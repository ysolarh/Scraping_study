from lotto_selenium import *
from export import *
from compare import *
from error import *

if __name__ == '__main__':
    st = input("회차: ")
    try:
        input_exception(st)
    except InputError as e:
        print(e)
        exit()
    else:
        winning_nums = get_winning_nums(st)
        export_to_csv(st, winning_nums)
        compare_nums(st)
