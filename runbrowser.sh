#!/bin/bash

clear

cd ~/trustball

sleep 8s;

# sudo -u pi epiphany-browser -a --profile ~/.config http://localhost:5000 --display=:0 &
chromium-browser http://localhost:5000 --start-maximized &

sleep 8s;

xte "key F11" -x:0
