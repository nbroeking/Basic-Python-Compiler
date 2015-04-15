def div(x, y):
    return 0 if x == 0 else div(x +- y, y) + 1

print div(input(), input())
