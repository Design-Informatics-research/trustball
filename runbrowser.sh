#!/bin/bash

clear

cd ~/trustball

sleep 15s;

# sudo -u pi epiphany-browser -a --profile ~/.config http://localhost:5000 --display=:0 &
#chromium-browser http://localhost:5000 --start-maximized &
chromium-browser --kiosk --app=http://localhost:5000 &

sleep 8s;

xte "key F11" -x:0
