def hello(name):
    """This function provides a greetings message

    Arg: 
      name: requires name. 

    Returns: 
      Prints out a tailored greetings message. 
    """
    print("hello " + name)

hello("codingbee")


# now you can view this help info in repl mode like this:

# $ py
# Python 3.6.4 (default, Oct  2 2018, 09:39:42)
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import documentation_using_docstrings
# hello codingbee
# >>> help(documentation_using_docstrings.hello)

# this outputs: 

#Help on function hello in module documentation_using_docstrings:

#hello(name)
#    This function provides a greetings message

#    Arg:
#      name: requires name.

#    Returns:
#      Prints out a tailored greetings message.
#(END)

