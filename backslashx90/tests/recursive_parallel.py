def mul(x, y):
    return 0 if x == 0 or y == 0 else y + mul(x +- 1, y)

print mul(5,5)
