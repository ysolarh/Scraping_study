import pandas as pd


def get_user_input():
    return list(map(int, input().split()))


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
    df_cut = df.iloc[:, 3:]
    include = list(df_cut.isin(user_input).itertuples())[0][1:] #
    for i in range(len(include)):
        print("idx: ", i)
        print("val:", df_cut.iloc[0, i], include[i])
        if include[i]:
            print("inc")
            if i == 6:
                print("!")
                is_bonus = True
            count += 1
            matched_nums.append(df_cut.iloc[0, i])
    # include = list(df.iloc[:, 3:].isin(user_input).itertuples()) #
    # for i in range(len(include[0])):
    #     print(i)
    #     if include[0][i]:
    #         print(df.iloc[:, 3:].iloc[0, i])
    #         if i == 7:
    #             print("!")
    #             is_bonus = True
    #         count += 1
    #         matched_nums.append(df.iloc[0, i + 2])
    ranking = find_ranking(count, is_bonus)
    display_result(ranking, matched_nums)
