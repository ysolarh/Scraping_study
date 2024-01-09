import pandas as pd


def get_user_input():
    # user_input = input().split()
    user_input = list(map(int, input().split()))
    # print(user_input, type(user_input))
    return user_input


def find_ranking(count, is_bonus):
    if count == 7 or (count == 6 and not is_bonus):
        return 1
    elif count == 6 and is_bonus:
        return 2
    elif count == 5:
        return 3
    elif count == 4:
        return 4
    elif count == 3:
        return 5
    else:
        return 0


def display_result(ranking, matched_nums):
    if not ranking:
        print("당첨금 없습니다.")
    else:
        print(f"{ranking}등 입니다.")
        print("맞힌 숫자: " + ", ".join(list(map(str, matched_nums))))


def compare_nums(st):
    count = 0
    is_bonus = False
    matched_nums = []
    user_input = get_user_input()
    df = pd.read_csv(st + '회차.csv')
    # print(df.iloc[:, 3:].items())
    # print(df.loc[:, '1':'보너스'])
    # for col, num in df.iloc[:, 4:].items():
    #     num = num.astype(int)
    #     print("!", col, num, type(num))
    #     if num in user_input:
    #         if col == 6:
    #             is_bonus = True
    #         count += 1
    #         matched_nums.append(num)

    # for num in user_input:
    #     print(df.iloc[:, 3:].isin([str(num)]))
    #     if df.iloc[:, 3:].isin([num]):
    #         # if col == 6:
    #         #     is_bonus = True
    #         count += 1
    #         matched_nums.append(num)

    # print(user_input)
    # print(type(df.iloc[0, 3]))
    # print(df.iloc[:, 3:].isin(user_input))
    # for i in df.iloc[:, 3:].isin(user_input).items():

    include = list(df.iloc[:, 3:].isin(user_input).itertuples())
    # print("include", include)
    for i in range(len(include[0])):
        if include[0][i]:
            if i == 6:
                is_bonus = True
            count += 1
            matched_nums.append(df.iloc[0, i+2])
    ranking = find_ranking(count, is_bonus)
    display_result(ranking, matched_nums)
