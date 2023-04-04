#!/bin/bash

# Open the first terminal window
gnome-terminal -e "bash -c 'echo Backend Terminal; cd ./backend; python app.py; $SHELL'"

# Open the second terminal window
gnome-terminal -e "bash -c 'echo Frontend Terminal; cd ./frontend; npm start; $SHELL'"