def f(x):
    
    y = x + 3

    def pure():
        return 2

    y = y + pure()
    return y

def g():
    print 3
    return 2

def x(y):
    x = input()
    return x + y

print f(5)
print g()
print x(1)
