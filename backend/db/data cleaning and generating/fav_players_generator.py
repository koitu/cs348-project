from random import *
# should run this in backend/db/data. ex: (for windows): python '..\data cleaning and generating\fav_players_generator.py'


player_file = open("player.sql", 'r')
player_file_null = open("player_for_null.sql", 'r')
write_to_file = open("fav_players.sql", 'w')

players = []

# fill players
for line in player_file:
    for word in line.split():
        # this will be a player id, kinda janky
        if len(word) > 0 and word[0] == '(':
            players.append(word[1:-1])

for line in player_file_null:
    for word in line.split():
        # this will be a player id, kinda janky
        if len(word) > 0 and word[0] == '(':
            players.append(word[1:-1])


user_start_id = 200001
user_amount = 10

write_to_file.write("INSERT INTO Fav_Players VALUES\n")

for i in range(user_amount):
    user_id = user_start_id + i
    indices = sample(range(len(players)), randint(0, 20))
      
    for count, j in enumerate(indices):
        player_id = players[j]
        write_to_file.write("\t\t(" + str(user_id) + ',' + str(player_id)  + ")")
        if i == user_amount - 1 and count == len(indices) - 1:
            write_to_file.write(";\n")
        else:
            write_to_file.write(",\n")

player_file.close()
player_file_null.close()
write_to_file.close()
