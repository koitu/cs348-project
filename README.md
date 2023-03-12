# cs348-project

## Milestone Reports
Reports are under their respective milestone folders

## Dependencies
You will need to have node.js and Python installed:

- https://www.python.org/downloads/
- https://nodejs.org/en/download/

Then to install the Python libraries run:
```
python3 -m pip install -r requirements.txt
```

## Usage

### Database Initialization
Install MySQL on your computer then go into the `backend/` folder.

Configure `config.ini` with your MySQL password and username and run:
```
python3 app.py --init-db
```

### Running the Project
You can either run the run command written in powershell (windows) or the bashscript file (MacOS and linux)
found in the project main directory, or

1. open a terminal and go to the `backend/` and run `python app.py` (python3 in MacOS)
2. open a second terminal and go to `frontend/` and run `npm start`.

## Backend Samples
Get a player from their player id:
```
$ curl -s 127.0.0.1:5000/api/players/8478421 | json_pp
```
```
{
   "birthday" : "Sat, 14 Dec 1996 00:00:00 GMT",
   "nationality" : "CAN",
   "picture" : null,
   "player_id" : 8478421,
   "player_name" : "A.J. Greer",
   "position" : null
}
```

Searching for players by their name:
```
$ curl -s 127.0.0.1:5000/api/players/ -X GET \
   -H 'Content-Type: application/json' \
   -d '{ "player_name": "en" }' | json_pp
```
```
{
   "players" : [
      {
         "birthday" : "Tue, 29 Jul 1997 00:00:00 GMT",
         "nationality" : "CAN",
         "picture" : 196,
         "player_id" : 8478425,
         "player_name" : "Brendan Guhle",
         "position" : "D"
      },
      {
         "birthday" : "Fri, 23 May 1997 00:00:00 GMT",
         "nationality" : "USA",
         "picture" : 182,
         "player_id" : 8478424,
         "player_name" : "Jansen Harkins",
         "position" : "C"
      }
   ]
}
```
