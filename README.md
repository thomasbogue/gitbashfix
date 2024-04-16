# gitbashfix
This python program modifies git-bash to run conda and python intuitively for Windows users

## Usage:
run the gitbashfix.py file in python or the gitbashfix.ipynb file in jupyter notebook.  If successfull this program should say
```
fix successfully applied
```

## Methods
This file checks to make sure the user is running Windows, and if so appends four lines of code to .bashrc, using environment variables to determine the home folder and the username.  These lines allow compatibility between git-bash and conda and python

## Known issues
If the user's home folder isn't in c:\Users, there is likely to be an issue.  Code will abort in this case.
