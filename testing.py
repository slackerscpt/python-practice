
import numpy as np
import pandas as pd


df = pd.read_csv('Tuesday-2019-Stats.csv')
print(df)

newData = {
    "Week": 30,
    "Date":  "03/17/2020",
    "Gm1": 300,
    "Gm2": 300,
    "Gm3": 300,
    "SS": 900,
    "HCP": 129,
    "HS": 1029,
    "Avg<br />Before": 202,
    "Avg<br />After": 202,
    "Todays<br />Avg": 300,
    "+/-<br />Avg": 85
}

df.loc[df.shape[0]] = [29, "03/17/2020", 300, 300, 300, 900, 129, 1029, 202, 202, 300, 85]
print(df)

df = df.append(newData, ignore_index=True)

print (df)

print(df.mean())
print(df.count())
print(df.sum())

games = df[['Gm1', 'Gm2', 'Gm3']].sum()
game_count = 3 * df['Gm1'].count()
print(games)
print (game_count)
total_pins = 0
for value in games:
    total_pins += value

print (total_pins)
print (total_pins /game_count)

current_Average = int (total_pins / game_count)
max = total_pins + 900
max_average = max / (game_count + 3)

print (max_average)
print(max_average - current_Average)

differnce = max_average - current_Average
differnce_pins = int(max_average) * (game_count + 3)
needed = (differnce_pins - total_pins)
print (needed)
