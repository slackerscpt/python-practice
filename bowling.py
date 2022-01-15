import numpy as np
import pandas as pd
import os
import glob

def listFiles():
    csvFiles = [file for file in glob.glob("*.csv")]
    return csvFiles

def pickLeague(leagueFiles):
    for idx, val in enumerate(leagueFiles):
        print ('{}. {}'.format(idx, val))
    user_pick = int(input("Which league data: "))

    leagueData = pd.read_csv(leagueFiles[user_pick])
    return leagueData

def leagueStats(leagueData):
    print (*leagueData[['Gm1', 'Gm2', 'Gm3']].mean())
    #* removes header and dtype
    print (max(leagueData[['Gm1', 'Gm2', 'Gm3']].max()))
    total_pins = sum(leagueData[['Gm1', 'Gm2', 'Gm3']].sum())
    game_count = 3 * leagueData['Gm1'].count()
    print ('League Average: {}'.format(int(total_pins/game_count)))

leagueFiles = listFiles()
leagueData = pickLeague(leagueFiles)
leagueStats(leagueData)


