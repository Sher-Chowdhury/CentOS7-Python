# https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
class Rectangle:

   # this is an instance method with the special name of "__init__". This gets executed automatically when you instantiate a new object. 
   # The first argument is the name given to label the object itself. This by convention is set to 'self', but I've changed it 
   # to 'myself' to show it's possible to change this.  
   def __init__(myself, given_length, given_breadth, given_unit_cost=0):
       myself.length = given_length
       myself.breadth = given_breadth
       myself.unit_cost = given_unit_cost
   
   def get_perimeter(myself):
       return 2 * (myself.length + myself.breadth)
   
   def get_area(myself):
       return myself.length * myself.breadth
   

   # no need to create an object to use the following static method
   def futureunitcost():
       return 10


# no need to create an object to use the following static method
print(Rectangle.futureunitcost())


r = Rectangle(given_length=160, given_breadth=120, given_unit_cost=2000)
# the following shorthand is also allowed
# r = Rectangle(160, 120, 2000)

# here's how to access an object's attributes. You shouldn't do this but is useful for debugging code. 
print(r.length)
print(type(r.length))
print(r.breadth)

print(r.get_area())
