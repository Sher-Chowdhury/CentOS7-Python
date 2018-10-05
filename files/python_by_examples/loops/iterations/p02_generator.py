# functions can return multiple values by using the: 
# return var1,var2....etc
# syntax. 
# you can also do a similar thing using the 'yield' keyword.  













fruits = ['apple', 'oranges', 'banana', 'plum']

fruits_iterator = iter(fruits)

# we now use the 'next' builtin function
# https://docs.python.org/3.3/library/functions.html



def fruits():
  yield 'apple'
  yield 'oranges'
  yield 'banana'
  yield 'plum'

fruit = fruits()

print(type(fruit))
print(next(fruit))
print(next(fruit))
print(next(fruit))
print(next(fruit))
