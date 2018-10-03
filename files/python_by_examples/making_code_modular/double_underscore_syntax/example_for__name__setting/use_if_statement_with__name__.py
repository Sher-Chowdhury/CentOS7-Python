#!/usr/bin/env python3.6

if __name__ == "__main__":
    print("This script has been executed directory from the bash terminal: " + __name__)
else: 
    print("This script was by importing via the REPL, or imported from anther script: " + __name__)


# One of most common use cases for this if statement 
# is to be able to make it easy to import a script's functions
# without executing the functions themselves, and also 
# also be able to run the script directly, with the intention of executing all the 
# functions. 


