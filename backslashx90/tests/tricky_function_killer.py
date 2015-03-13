w = 6
def tricky0(y):
    v = 1
    def tricky1(x):
        u = 3
        def tricky2(z):
            t = 2
            return x + y + z + w + v+ u + t
        return lambda x: tricky2(x)
    return tricky1

print tricky0(5)(2)(1)
