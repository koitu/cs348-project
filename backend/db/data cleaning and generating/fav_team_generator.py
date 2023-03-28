from random import *
# should run this in backend/db/data like so (for windows): python '..\data cleaning and generating\fav_team_generator.py'
#much simpler logic, teams have ids from [101,132]

write_to_file = open("fav_teams.sql", 'w')


user_start_id = 200001
user_amount = 10

write_to_file.write("INSERT INTO Fav_Teams VALUES\n")

for i in range(user_amount):
    user_id = user_start_id + i
    team = sample(range(197, 228 + 1), randint(0, 20))
      
    for count, j in enumerate(team):
        write_to_file.write("\t\t(" + str(user_id) + ',' + str(j)  + ")")
        if i == user_amount - 1 and count == len(team) - 1:
            write_to_file.write(";\n")
        else:
            write_to_file.write(",\n")

write_to_file.close()

