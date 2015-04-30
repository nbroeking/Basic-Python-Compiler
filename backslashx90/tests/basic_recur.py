def rec(x):
    y = x +- 1
    print x
    return 0 if x == 0 else rec(y)

rec(5)
