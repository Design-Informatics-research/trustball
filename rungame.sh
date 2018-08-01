#!/bin/bash

clear

cd ~/trustball

lxterminal -e sudo python reset.py

sleep 8s;

lxterminal -e sudo FLASK_APP=trustball.py flask run
