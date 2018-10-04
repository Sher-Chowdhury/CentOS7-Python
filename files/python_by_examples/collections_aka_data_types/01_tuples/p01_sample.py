# lists and tuples are similar. The main difference is that
# lists can be modifled (aka mutuable) whereas tuples can't be modified (aka immutable)



this_is_a_list = ['hello', 42, 0.5]

print(type(this_is_a_list))
print(type(this_is_a_list[1]))
print(this_is_a_list[1])


# Similar to lists, but this time uses round brackets
this_is_a_tuple = ('hello', 99, 0.5)

print(type(this_is_a_tuple))
print(type(this_is_a_tuple[1]))
print(this_is_a_tuple[1])

