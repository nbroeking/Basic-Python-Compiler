def map_sum(f, x, y):
    return f(x) + f(y)

def addOne(x):
    y = 0
    lst = [1,2,4]
    while y != 10000000:
        y = y + lst[2] +- (lst[1] + lst[0])
    y = y +- 9999999
    x = x + y
    return x

x = map_sum(addOne, 4, 5)
y = map_sum(addOne, 5, 6)
z = map_sum(addOne, 7, 8)
w = map_sum(addOne, 9, 10)
v = map_sum(addOne, 11, 12)

print x + y +- z + w +- v
