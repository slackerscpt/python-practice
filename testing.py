
import numpy as np
import pandas as pd


def increaseAverage(total_pins, total_games):
    print('-- Checking Averages --')
    print (total_pins)
    print (total_games)
    current_Average = int (total_pins / total_games)
    max_average = (total_pins + 900) / (total_games + 3)

    min_average = total_pins / (total_games + 3)
    high_diff = (int(max_average) * (total_games + 3)) - total_pins


    print (min_average)
    print (current_Average)
    print (max_average)


df = pd.read_csv('Tuesday-2019-Stats.csv')
print(df)

    # How to add data to datafram
    # newData = {
    #     "Week": 30,
    #     "Date":  "03/17/2020",
    #     "Gm1": 300,
    #     "Gm2": 300,
    #     "Gm3": 300,
    #     "SS": 900,
    #     "HCP": 129,
    #     "HS": 1029,
    #     "Avg<br />Before": 202,
    #     "Avg<br />After": 202,
    #     "Todays<br />Avg": 300,
    #     "+/-<br />Avg": 85
    # }

    # df.loc[df.shape[0]] = [29, "03/17/2020", 300, 300, 300, 900, 129, 1029, 202, 202, 300, 85]
    # print(df)

    # df = df.append(newData, ignore_index=True)

    # print (df)

# print(df.mean())
# print(df.count())
# print(df.sum())

total_pins = sum(df[['Gm1', 'Gm2', 'Gm3']].sum())
game_count = 3 * df['Gm1'].count()

increaseAverage(total_pins, game_count)

