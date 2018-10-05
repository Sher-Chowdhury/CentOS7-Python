# functions can return multiple values by using the: 
# return var1,var2....etc
# syntax. 
# you can also do a similar thing using the 'yield' keyword.  













fruits = ['apple', 'oranges', 'banana', 'plum']

fruits_iterator = iter(fruits)

# we now use the 'next' builtin function
# https://docs.python.org/3.3/library/functions.html


# a genarotor is simply a functions that contains one or more 'yield' lines. 
def fruits():
  print("about to print apple")
  yield 'apple'
  print("about to print oranges")
  yield 'oranges'
  print("about to print banana")
  yield 'banana'
  print("about to print plum")
  yield 'plum'

fruit = fruits()

print(type(fruit))

print(next(fruit))
print(next(fruit))
print(next(fruit))
print(next(fruit))


# the yield command effectively pauses the function until the next 'next' command is executed. 
