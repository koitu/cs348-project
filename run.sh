#!/bin/bash

# Open the first terminal window
gnome-terminal -e "bash -c 'echo Terminal 1; cd ./backend; python app.py; $SHELL'"

# Open the second terminal window
gnome-terminal -e "bash -c 'echo Terminal 2; cd ./frontend; npm start; $SHELL'"