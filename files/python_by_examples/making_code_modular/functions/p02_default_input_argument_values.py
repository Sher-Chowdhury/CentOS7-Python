# note, parameters without defaults, e.g. 'name' should be listed first.  
def hello(name, title="Mister"):
    print("hello " + title + " " + name)

hello("codingbee")
hello("codingbee", "Sir")

# if you want to be more explicit, or if you want to define arguments in different order.
hello(title="Doctor", name="codingbee")

