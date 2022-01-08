
import numpy as np
import pandas as pd


def increaseAverage(total_pins, total_games):
    print('-- Checking Averages --')
    current_Average = int (total_pins / total_games)
    max_average = int ((total_pins + 900) / (total_games + 3))
    min_average = int(total_pins / (total_games + 3))
    high_diff = (int(max_average) * (total_games + 3)) - total_pins


    #Need to take a range. 1 - max over
    #So if current is 200 and max is 204, want to determine what should be shot to get each average. 

    average_boosts = []    

    for i in range(1, (max_average - current_Average)+1):
        seek_average = current_Average + i
        seek_pins = (seek_average * (total_games + 3)) - total_pins
        average_boosts.append([seek_average, seek_pins])

    boost_data = pd.DataFrame(average_boosts, columns= ['Average', 'Series'])
    print (boost_data)

def readLeagues():
    leagueData = pd.read_csv('Leagues.csv')
    print (leagueData)
    activeLeagues = leagueData[leagueData['active'] == True]
    print (activeLeagues)



def getLeagueData(leagueFile):
    df = pd.read_csv(leagueFile)
    print(df)



    # print(df.mean())
    # print(df.count())
    # print(df.sum())

    total_pins = sum(df[['Gm1', 'Gm2', 'Gm3']].sum())
    game_count = 3 * df['Gm1'].count()

    increaseAverage(total_pins, game_count)

readLeagues()
getLeagueData(leagueFile='Tuesday-2019-Stats.csv')