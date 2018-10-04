def hello(name):
    print("hello " + name)

hello("codingbee")



def hello1(name):
    return "hello " + name


myresult = hello1("tom")

print(myresult)

# note, you always call functions using round brackets. Yoy may need to add content inside the round bracket, depending on what funtions you call. 
# A good example is the print() function


# A method is a type of fuction. It's a function that resides in a class. That means you call the method against an existing object of that class. E.g.
# object.methodname(potential_content_here) 
# we use a similar syntax when using functions from an imported .py script, see below.

# you can import this script into a REPL session by running the following on the repl command line:

#[root@pythonbox1 making_code_modular]# py
#Python 3.6.4 (default, Oct  2 2018, 09:39:42)
#[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import sample_functions
#hello codingbee
#hello tom
#>>> sample_functions.hello('jerry')         # Notice the similar syntax here. 
#hello jerry
#>>>


# you can also import specific function using the syntax:
# from {scriptname} import {functionname}
# here's an example:


# [root@pythonbox1 making_code_modular]# py
# Python 3.6.4 (default, Oct  2 2018, 09:39:42)
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from sample_functions import hello1
# hello codingbee
# hello tom
# >>> hello('bowser')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'hello' is not defined
# >>> hello1('bowser')
# 'hello bowser'
#>>>

