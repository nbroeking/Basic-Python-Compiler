class X:
    def __init__(self):
        self.x = 5

def myfunc(clazz):
    return clazz()

def other():
    ret = X()
    ret.x = 1
    return ret

x1 = myfunc(X)
x2 = myfunc(other)

print x1.x
print x2.x
