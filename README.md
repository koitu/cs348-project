# cs348-project

## Milestone Reports
Reports are under their respective milestone folders
- For SQL commands see `milestone 2/feature_queries`
- For backend api usage examples see `milestone 2/backend examples.md`

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
To load the sample data run:
```
python3 app.py --init-db-sample
```

### Running the Project
You can either run the run command written in powershell (windows) or the bashscript file (MacOS and linux)
found in the project main directory, or

1. open a terminal and go to the `backend/` and run `python app.py` (python3 in MacOS)
2. open a second terminal and go to `frontend/` and run `npm start`.
