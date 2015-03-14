w = 1
def test0(y):
    def test1(x):
        return x + y + w
    return test1

print test0(1)(2)
