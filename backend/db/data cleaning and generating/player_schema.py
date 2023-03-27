import pandas as pd
import sys
from urllib.request import urlopen


def inch_to_cm(height):
    foot = int(height[0])
    inch = int(height[2:-1])
    return int((12 * foot + inch) * 2.58)


# data cleaning
all_player_df = pd.read_csv('allPlayersLookup.csv', sep=',', header=0, dtype=str)
all_player_df['team'] = all_player_df['team'].replace('L.A', 'LAK')
all_player_df['team'] = all_player_df['team'].replace('N.J', 'NJD')
all_player_df['team'] = all_player_df['team'].replace('S.J', 'SJS')
all_player_df['team'] = all_player_df['team'].replace('T.B', 'TBL')
all_player_df = all_player_df.dropna()
all_player_df = all_player_df.drop(all_player_df[all_player_df.team == "ATL"].index)

output_string = "INSERT INTO Player VALUES\n"

# check if the profile picture can be achievable, if not, use a default one
for index, row in all_player_df.iterrows():
    url = 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/' + str(row['playerId']) + '.jpg'
    idx = row['name'].find("'")
    try:
        urlopen(url)
    except:
        if idx != -1:
            new_name = row['name'][:idx] + "'" + row['name'][idx:]
            output_string += "\t(" + row['playerId'] + ", '" + new_name + "', '" + row['birthDate'] + "', " + row['weight'][ 0:3] + ", " + str(
                inch_to_cm(row['height'])) + ", '" + row['team'] + "', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/skater.jpg', " + str(
                2023 - int(row['birthDate'][0:4])) + ", '" + row['position'] + "'),\n"
        else:
            output_string += "\t(" + row['playerId'] + ", '" + row['name'] + "', '" + row['birthDate'] + "', " + row['weight'][0:3] + ", " + str(
                inch_to_cm(row['height'])) + ", '" + row['team'] + "', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/skater.jpg', " + str(
                2023 - int(row['birthDate'][0:4])) + ", '" + row['position'] + "'),\n"
    else:
        if idx != -1:
            new_name = row['name'][:idx] + "'" + row['name'][idx:]
            output_string += "\t(" + row['playerId'] + ", '" + new_name + "', '" + row['birthDate'] + "', " + row['weight'][0:3] + ", " + str(
                inch_to_cm(row['height'])) + ", '" + row['team'] + "', '" + url + "', " + str(
                2023 - int(row['birthDate'][0:4])) + ", '" + row['position'] + "'),\n"
        else:
            output_string += "\t(" + row['playerId'] + ", '" + row['name'] + "', '" + row['birthDate'] + "', " + row['weight'][ 0:3] + ", " + str(
                inch_to_cm(row['height'])) + ", '" + row['team'] + "', '" + url + "', " + str(
                2023 - int(row['birthDate'][0:4])) + ", '" + row['position'] + "'),\n"
# output the string
write_string = output_string[:-2] + ';'
f = open("player.sql", 'w')
f.write(write_string)
f.close()
