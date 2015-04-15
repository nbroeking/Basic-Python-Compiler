x = 4

class hello:
    y = 3 # -> set_attr(hello, y, 3)
    if 1:
        x = 1 # -> set_attr(hello, x, 1)
    else:
        print 7
    print x

print x
