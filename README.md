# p9acme-util

A repository with various scripts and programs used to interact with the Acme
editor.

Russ Cox's [video](https://www.youtube.com/watch?v=dP1xVpMPn8M) is an
excellent introduction to Acme.


## bin

`a` : used for starting acme

`sc+` : comment region Standard ML style -- (* ... *)

`sc-` : uncomment region commented using `sc+`

`T4` : convert tabs to 4 spaces -- useful when working with Python

`i+` : indent region by 1 Tab

`i-` : de-indent region by 1 Tab

Usually, these scripts (with the exclusion of `a`) are placed in the tag prepended
with the `|` character. 


## pyacme

A python wrapper around plan9port's `9p` command. Makes it easy to write
python scripts that interact with Acme.

### Usage

```
#!/usr/bin/python

import pyacme

winid = pyacme.windownew() # creates a new window
pyacme.write("clean", winid, "ctl") # mark window as clean
pyacme.write("PYACME", winid, "body') # write to the window's body

pyacme.read(winid, "body") # read from the window's body
```
