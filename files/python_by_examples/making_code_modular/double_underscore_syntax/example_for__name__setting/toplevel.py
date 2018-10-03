#!/usr/bin/env python3.6

import secondlevel

# __name__ is a special environment that's used to keep track of what level a piece of code is being executed. 
# if a script is being run directly, then __name__ is equal to the string "__main__" within that script's scope. 
# however if the main script (in our case is called toplevel) imports another script, e.g. secondlevel, then __name__
# value inside the second script is equal to the script's name itself. 

print(__name__)



# $ py secondlevel.py
# __main__
# $ py toplevel.py
# secondlevel
# __main__

print(secondlevel.__file__)
