z = 6

def g(x):
    return x + z

def return_g():
    z = 2
    def g(x):
        return x + z
    return g

f = return_g()
print f(2)
f = g
z = 8
print f(2)
