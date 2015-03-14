def test0(y):
    def test1(x):
        return x + y
    return test1

print test0(1)(2)
