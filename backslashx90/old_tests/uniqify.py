def x():
    def y():
        print 1
    x = 5
    print x

def another():
    
    def y():
        print 2

    x = 4
    print x

x = 4
print x
another()
another()
print x
