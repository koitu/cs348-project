# cs348-project

## Dependencies
You will need to have node.js and Python installed:

- https://www.python.org/downloads/
- https://nodejs.org/en/download/

Then to install the Python libraries run:
```
python3 -m pip install -r requirements.txt
```

## Usage
you can either run the run command written in powershell (windows) or the bashscript file (MacOS and linux)
found in the project main directory, or

1. open a terminal and go to the `backend/` and run `python app.py` (python3 in MacOS)
2. open a second terminal and go to `frontend/` and run `npm start`.

TODO: how to set up the database


## Samples
TODO: sample api calls to do with curl

Get a user from their account id:
```
$ curl -s 127.0.0.1:5000/api/users/3 | json_pp
{
   "account_id" : "3",
   "email" : null,
   "fullname" : "Kenley Mcguire",
   "profile_pic" : "/static/default_profile_pic.png",
   "username" : null
}
```

Get a player from their player id:
```
$ curl -s 127.0.0.1:5000/api/players/3 | json_pp
{
   "birthday" : null,
   "nationality" : null,
   "picture" : null,
   "player_id" : "3",
   "player_name" : "Roger Federer",
   "position" : null
}
```
