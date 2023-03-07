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
Install MySQL on your computer.

Configure the `backend/config.ini` with your MySQL password and username then run one of the two commands:
1. `.\init.ps1` and close the terminal that is opened, or
2. `cd backend/` and `python app.py --init-db`

### Running the Project
You can either run the run command written in powershell (windows) or the bashscript file (MacOS and linux)
found in the project main directory, or

1. open a terminal and go to the `backend/` and run `python app.py` (python3 in MacOS)
2. open a second terminal and go to `frontend/` and run `npm start`.

## Samples
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
