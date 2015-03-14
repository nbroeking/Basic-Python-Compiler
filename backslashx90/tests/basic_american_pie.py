def x(y):
    return [] if y == 0 else [y] + x(y+-1)
print x(1)
