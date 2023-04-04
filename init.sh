#!/bin/bash

# Open the first terminal window
gnome-terminal -e "bash -c 'echo Backend Terminal; python3 -m pip install -r requirements.txt; cd ./backend; python3 app.py --init-db; $SHELL'"

# Open the second terminal window
gnome-terminal -e "bash -c 'echo Frontend Terminal; cd ./frontend; npm install -f; $SHELL'"