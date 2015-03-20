def even(x):
    return True if x == 0 else (False if x == 1 else even(x +- 2))

print even(2)
