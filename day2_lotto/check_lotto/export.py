import pandas as pd


def export_to_csv(st, winning_nums):
    columns = ['회차', '추첨일', '1등', '1', '2', '3', '4', '5', '6', '보너스']
    df = pd.DataFrame(columns=columns)
    df.loc[0] = winning_nums
    df.to_csv(st + "회차.csv", index=False)
