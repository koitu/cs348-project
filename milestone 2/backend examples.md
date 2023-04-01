# Backend Examples
Some examples of what has been implemented into the backend.

To begin load up the production data and start the backend:
```
python backend/app.py --init-db
python backend/app.py
```

## User
### Creating a new user
```
curl -s 127.0.0.1:5000/api/users?username=redpuppy
```
```
{"users":[]}
```
We see that there does not exist any users with username `redpuppy` so we register
```
curl -s 127.0.0.1:5000/api/users/ -X POST \
   -H 'Content-Type: application/json' \
   -d '{ "username": "redpuppy", "email": "someone@something.com", "password": "123", "fullname": "Full Name"}'
```
```
{"status":"OK"}
```
Now the user has been created
```
curl -s 127.0.0.1:5000/api/users?username=redpuppy | json_pp
```
```
{
   "users" : [
      {
         "account_id" : 99357,
         "email" : "someone@something.com",
         "fullname" : "Full Name",
         "is_admin" : false,
         "profile_pic" : "/static/default_profile_pic.png",
         "username" : "redpuppy"
      }
   ]
}
```

### Attempt to login
Logging in with the incorrect password
```
curl -s "127.0.0.1:5000/api/users/login?username=yellowswan194&password=wrong"
```
```
{"status":"BAD"}
```
Logging in with the correct password
```
curl -s "127.0.0.1:5000/api/users/login?username=yellowswan194&password=iVFEhBJHCMGP0GI"
```
```
{"id":81262,"status":"OK"}
```

### Get a user's followed players
```
curl -s http://127.0.0.1:5000/api/users/200003/players | json_pp
```
```
{
   "players" : [
      {
         "birthday" : "Fri, 01 Jul 1977 00:00:00 GMT",
         "height" : 188,
         "nationality" : "CAN",
         "number" : 46,
         "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8462042.jpg",
         "player_id" : 8462042,
         "player_name" : "Jarome Iginla",
         "position" : "R",
         "weight" : 210
      },
...
```

### Get a user's followed teams
```
curl -s http://127.0.0.1:5000/api/users/200003/teams | json_pp
```
```
   "teams" : [
      {
         "abbrv" : "ANA",
         "location" : "Honda Center",
         "logo_url" : "https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Anaheim_Ducks.svg/330px-Anaheim_Ducks.svg.png",
         "since" : "1993",
         "team_id" : 197,
         "team_name" : "Anaheim Ducks"
      },
...
```

### Add a team to a user's followed
We check and find that user is not following any teams
```
curl -s 127.0.0.1:5000/api/users/13230/teams
```
```
{"teams":[]}

```
Add the team with id 200 to the list of followed teams
```
curl -s -X POST 127.0.0.1:5000/api/teams/200/followers?account_id=13230
```
```
{"status":"OK"}
```
check and find that the user is now following the team
```
curl -s 127.0.0.1:5000/api/users/13230/teams | json_pp
```
```
{
   "teams" : [
      {
         "abbrv" : "BUF",
         "location" : "KeyBank Center",
         "logo_url" : "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Buffalo_Sabres_Logo.svg/330px-Buffalo_Sabres_Logo.svg.png",
         "since" : "1970",
         "team_id" : 200,
         "team_name" : "Buffalo Sabres"
      }
   ]
}

```
Very similar method for adding a player

## Player

### Get a player by player_id
```
curl -s 127.0.0.1:5000/api/players/8468510 | json_pp
```
```
{
   "birthday" : "Thu, 19 Feb 1981 00:00:00 GMT",
   "height" : 193,
   "nationality" : "MIN",
   "number" : 42,
   "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/skater.jpg",
   "player_id" : 8468510,
   "player_name" : "Jeff Taffe",
   "position" : "L",
   "weight" : 207
}
```

### Search for player by their name
```
curl -s 127.0.0.1:5000/api/players?name=Jason | json_pp
```
```
{
   "players" : [
      {
         "birthday" : "Sun, 03 Jun 1990 00:00:00 GMT",
         "height" : 180,
         "nationality" : "CAN",
         "number" : 33,
         "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8475917.jpg",
         "player_id" : 8475917,
         "player_name" : "Jason Akeson",
         "position" : "R",
         "weight" : 185
      },
      {
         "birthday" : "Fri, 11 Oct 1974 00:00:00 GMT",
         "height" : 198,
         "nationality" : "CAN",
         "number" : 49,
         "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8459429.jpg",
         "player_id" : 8459429,
         "player_name" : "Jason Arnott",
         "position" : "C",
         "weight" : 220
      },
...
```

### Get players in a team
```
curl -s 127.0.0.1:5000/api/players?team_id=200 | json_pp
```
```
{
   "players" : [
      {
         "birthday" : "Thu, 04 May 1989 00:00:00 GMT",
         "height" : 185,
         "nationality" : "CAN",
         "number" : 34,
         "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8477180.jpg",
         "player_id" : 8477180,
         "player_name" : "Aaron Dell",
         "position" : "G",
         "weight" : 205
      },
      {
         "birthday" : "Thu, 15 Feb 1979 00:00:00 GMT",
         "height" : 188,
         "nationality" : "CAN",
         "number" : 44,
         "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8466216.jpg",
         "player_id" : 8466216,
         "player_name" : "Adam Mair",
         "position" : "C",
         "weight" : 208
      },
...
```

## Team

### Search teams by name
```
curl -s 127.0.0.1:5000/api/teams?name=new | json_pp
```
```
{
   "teams" : [
      {
         "abbrv" : "NJD",
         "location" : "Prudential Center",
         "logo_url" : "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/New_Jersey_Devils_logo.svg/330px-New_Jersey_Devils_logo.svg.png",
         "since" : "1974",
         "team_id" : 213,
         "team_name" : "New Jersey Devils"
      },
      {
         "abbrv" : "NYI",
         "location" : "UBS Arena",
         "logo_url" : "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/Logo_New_York_Islanders.svg/330px-Logo_New_York_Islanders.svg.png",
         "since" : "1972",
         "team_id" : 215,
         "team_name" : "New York Islanders"
      },
...

```

### Get information about a specific team
```
curl -s 127.0.0.1:5000/api/teams/200 | json_pp
```
```
{
   "abbrv" : "BUF",
   "location" : "KeyBank Center",
   "logo_url" : "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Buffalo_Sabres_Logo.svg/330px-Buffalo_Sabres_Logo.svg.png",
   "since" : "1970",
   "team_id" : 200,
   "team_name" : "Buffalo Sabres"
}
```

## Match

### Get matches played by a team
Get matches played between team id 204 and 205 (order by date)
```
curl -s 127.0.0.1:5000/api/matches?team_ids=204,205 | json_pp
```
```
{
   "matches" : [
      {
         "date" : "Thu, 12 Jan 2023 00:00:00 GMT",
         "location" : "United Center",
         "match_id" : 2022020671,
         "season" : "2022",
         "team_away_id" : 205,
         "team_away_score" : 2,
         "team_home_id" : 204,
         "team_home_score" : 3
      },
      {
         "date" : "Fri, 28 Jan 2022 00:00:00 GMT",
         "location" : "United Center",
         "match_id" : 2021020769,
         "season" : "2021",
         "team_away_id" : 205,
         "team_away_score" : 6,
         "team_home_id" : 204,
         "team_home_score" : 4
      },
...
```

### Get matches played by a player
```
curl -s 127.0.0.1:5000/api/matches?player_ids=8466216 | json_pp
```
```
{
   "matches" : [
      {
         "date" : "Sun, 10 Apr 2011 00:00:00 GMT",
         "location" : "TD Garden",
         "match_id" : 2010021226,
         "season" : "2010",
         "team_away_id" : 213,
         "team_away_score" : 3,
         "team_home_id" : 199,
         "team_home_score" : 2
      },
...
```
