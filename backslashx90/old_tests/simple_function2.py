y = 2
def my_function(x):
    print x(5, y)

def lam(x,y):
    return x + y

my_function(lam)
