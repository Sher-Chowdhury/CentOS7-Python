# everuthing is an object. Here we instantiated an object called x and we specified that it is instantiated from the integer class:
x = int(5)

# the above is commonly used in the implicit form:
# x = 5


print(x)

# in case you don't know what class an object was instantiated from, and want to find out, then do:

print(type(x))


y = "hello world"
print(y)
print(type(y))

# the following prints all the public methods available in the str class. 
print(dir(str))

# you can use the builtin help function in repl mode to read man page for this class's public methods:
# help(str)

# here's an example of applying the string class's upper public method:
print(y.upper())
# https://docs.python.org/2/library/stdtypes.html#str.upper
