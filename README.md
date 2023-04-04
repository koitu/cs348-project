# cs348-project

## Milestone Reports
The main code source for the project is in the `backend/` and `frontend/` directories, but you can find a copy of required files for each milestone in the corresponding `milestoneX/` directory. 

Reports are also available in each milestone's directory.


## Dependencies
You will need to have node.js and Python installed:

- https://www.python.org/downloads/
- https://nodejs.org/en/download/

Then run the `init` script in the root directory, which does the following:
- Installs the python dependencies
- Installs the node dependencies

For Windows:
```
./init.ps1
```
For MacOS and Linux:
```
./init.sh
```

## Usage

### Database Initialization
- Install MySQL on your computer 
- Go into the `backend/` directory
- Configure `config.ini` with your MySQL username and password 
- Initialize and populate the database by running the following commands:
```
python3 app.py --init-db
```
To load the sample data run:
```
python3 app.py --init-db-sample
```

### Running the Project
You can use the provided `run` script in the root directory to run the project:

For Windows:
```
./run.ps1
```
For MacOS and Linux:
```
./run.sh
```

