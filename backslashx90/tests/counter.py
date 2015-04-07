def count(x):
    print x
    return 0 if x == 0 else count(x +- 1)

count(100)
