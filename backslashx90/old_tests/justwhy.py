class x:
    class y:
        i = 3

        def printer(self):
            print x.y.i

if 1:
    x.w = 4
    x.y.i = x.w

else:
    print 6

r = x.y()
r.printer()
