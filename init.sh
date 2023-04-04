#!/bin/bash

# Open the first terminal window
gnome-terminal -e "bash -c 'echo Backend Terminal; python3 -m pip install -r requirements.txt; $SHELL'"

# Open the second terminal window
gnome-terminal -e "bash -c 'echo Frontend Terminal; cd ./frontend; npm install -f; $SHELL'"