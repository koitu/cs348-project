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
$ curl -s 127.0.0.1:5000/api/players/8468510 | json_pp
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

Searching for players by their name:
```
$ curl -s 127.0.0.1:5000/api/players/ -X GET \
   -H 'Content-Type: application/json' \
   -d '{ "player_name": "son" }' | json_pp
```
```
{
   "players" : [
      {
         "birthday" : "Sat, 30 Apr 1983 00:00:00 GMT",
         "height" : 188,
         "nationality" : "BOS",
         "number" : 40,
         "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8469534.jpg",
         "player_id" : 8469534,
         "player_name" : "Aaron Johnson",
         "position" : "D",
         "weight" : 204
      },
      {
         "birthday" : "Wed, 30 Nov 1988 00:00:00 GMT",
         "height" : 188,
         "nationality" : "FLA",
         "number" : 35,
         "picture" : "https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8476200.jpg",
         "player_id" : 8476200,
         "player_name" : "Paul Thompson",
         "position" : "R",
         "weight" : 200
      }
   ]
}
```
