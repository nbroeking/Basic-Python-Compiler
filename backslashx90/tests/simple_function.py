y = 2
def my_function(x):
    print x(5, y)

print my_function(lambda x, y: x + y)
