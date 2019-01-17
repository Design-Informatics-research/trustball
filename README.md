## Starting trustball

To run, start buttons and start server: 
 
`sudo FLASK_APP=trustball.py flask run`

Or use the start script: `./rungame.sh`.

If the application doesn't start it's likely caused by an issue in controlling the motors, see debugging instructions below.

Once it's running open a browser at http://localhost:5000, try refreshing 
after 20 seconds if you don't see the start page.


## Debugging and Troubleshooting

### Test motor controller hat

To see connection address:

`sudo i2cdetect -y 1`

You should see several columns and rows, and in one cell a value e.g. '40' representing the address of the device.

Try this a few times, if the value shows then goes away, it's possible
not enough power isn't reaching the device or there's a shortage.

Check the controller contacts, sometimes the hat can push down on the top 
of the RPi on one side. Just lift it up a bit or reconnect it.

### Test motors:

Run:

`sudo python reset.py`

If motors don't move, check cables, make sure they are plugged in with white
cable on the inside, and black cable on the edge.

If you get a `Remote I/O error`, try testing the motor controller as described
abive.

