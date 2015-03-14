def mul(x, y):
    return 0 if x == 0 or y == 0 else x + mul(x, y +- 1)

print mul(5,5)
