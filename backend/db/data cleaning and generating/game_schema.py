import pandas as pd
import sys

# team mapping
team_to_id = {"ANA":197, "ARI":198, "BOS":199, "BUF":200, "CAR":201, "CBJ":202, "CGY":203, "CHI":204, "COL":205, "DAL":206, "DET":207, "EDM":208, "FLA":209, "LAK":210, "MIN":211, "MTL":212, "NJD":213, "NSH":214, "NYI":215, "NYR":216, "OTT":217, "PHI":218, "PIT":219, "SEA":220, "SJS":221, "STL":222, "TBL":223, "TOR":224, "VAN":225, "VGK":226, "WPG":227, "WSH":228}

# data cleaning
all_game_df = pd.read_csv('all_teams.csv', sep=',', header=0, dtype = str)[['season','gameId','playerTeam','opposingTeam','home_or_away','gameDate']]
all_game_df = all_game_df.drop_duplicates()
all_game_df['playerTeam'] = all_game_df['playerTeam'].replace('L.A','LAK')
all_game_df['playerTeam'] = all_game_df['playerTeam'].replace('N.J','NJD')
all_game_df['playerTeam'] = all_game_df['playerTeam'].replace('S.J','SJS')
all_game_df['playerTeam'] = all_game_df['playerTeam'].replace('T.B','TBL')
all_game_df['opposingTeam'] = all_game_df['opposingTeam'].replace('L.A','LAK')
all_game_df['opposingTeam'] = all_game_df['opposingTeam'].replace('N.J','NJD')
all_game_df['opposingTeam'] = all_game_df['opposingTeam'].replace('S.J','SJS')
all_game_df['opposingTeam'] = all_game_df['opposingTeam'].replace('T.B','TBL')
all_game_df = all_game_df.drop(all_game_df[all_game_df.playerTeam=="ATL"].index)
all_game_df = all_game_df.drop(all_game_df[all_game_df.opposingTeam=="ATL"].index)
all_game_df = all_game_df.drop(all_game_df[all_game_df.home_or_away=="AWAY"].index)
all_game_df = all_game_df.dropna()
# all_game_df = all_game_df.loc[[5,200,400,1000,1300,1600,1900,2300,2500,2900]]

output_string = "INSERT INTO Game VALUES\n"

# check if the profile picture can be achievable, if not, use a default one
for index, row in all_game_df.iterrows():
  date = row['gameDate'][0:4]+'-'+row['gameDate'][4:6]+'-'+row['gameDate'][6:8]
  output_string += "\t("+row['gameId']+", "+row['season']+", \""+date+"\", "+str(team_to_id[row['playerTeam']])+", "+str(team_to_id[row['opposingTeam']])+"),\n"


write_string = output_string[:-2] + ';'
f=open("game.sql",'w')
f.write(write_string)
f.close()
