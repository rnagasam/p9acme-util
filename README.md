# pyacme

A python wrapper around plan9port's `9p` command. Makes it easy to write
python scripts that interact with Acme.

Russ Cox's [video](https://www.youtube.com/watch?v=dP1xVpMPn8M) is
an excellent introduction to Acme.

## Usage


```
#!/usr/bin/python

import pyacme

winid = pyacme.windownew() # creates a new window
pyacme.write("clean", winid, "ctl") # mark window as clean
pyacme.write("PYACME", winid, "body') # write to the window's body

pyacme.read(winid, "body") # read from the window's body
```
