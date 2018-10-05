# https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
class Rectangle:

   # this is an instance method with the special name of "__init__". This gets executed automatically when you instantiate a new object. 
   # The first argument is the name given to label the object itself. This by convention is set to 'self', but I've changed it 
   # to 'myself' to show it's possible to change this.  
   def __init__(myself, length, breadth, unit_cost=0):
       myself.length = length
       myself.breadth = breadth
       myself.unit_cost = unit_cost
   
   def get_perimeter(myself):
       return 2 * (myself.length + myself.breadth)
   
   def get_area(myself):
       return myself.length * myself.breadth
   

   # no need to create an object to use the following static method
   def futureunitcost():
       return 10


# no need to create an object to use the following static method
print(Rectangle.futureunitcost())


r = Rectangle(160, 120, 2000)
print(r.get_area())
