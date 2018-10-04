# https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
def hello(var1, var2):
    x =  var1 * 100
    y = var2 * 1000
    return x, y

# this function returns multiple values, and here's how to capture them. 
xvalue, yvalue = hello(3,5)
print(xvalue)
print(yvalue)



zvalue = hello(2,4)
print(zvalue[0])
print(zvalue[1])
