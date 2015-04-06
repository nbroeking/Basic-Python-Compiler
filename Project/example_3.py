def outer():
    x = []
    y = []

    def inner():
        for i in xrange(0, 500):
            x.append(i)
        
        for i in xrange(0, 1000):
            x.append(i)
            y.append(i)

    inner()

    print(x)
    print(y)
