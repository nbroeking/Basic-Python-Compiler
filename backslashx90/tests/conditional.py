def condition(f):
    x = 0
    while x != 10:
        x = f(x)
    return f(x)

def addOne(x):
    y = 0
    lst = [1,2,4]
    while y != 100000:
        y = y + lst[0] +- (lst[1] + lst[2])
    y = y +- 99999
    x = x + y
    return x

x = condition(addOne)
y = condition(addOne)
z = condition(addOne)
w = condition(addOne)
v = condition(addOne)

print x + y +- z + w +- v
