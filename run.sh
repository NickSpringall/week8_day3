# /bin/bash

# check if python is installed
python3 -m venv todo-venv
# check if venv already exists
source todo-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py

