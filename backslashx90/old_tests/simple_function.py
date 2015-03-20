y = 2
def my_function(x):
    print x(5, y)

my_function(lambda x, y: x + y)
