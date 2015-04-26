def conditional_pure(f, x):
    return f(x)

def much(x):
    while x != 10000000:
        x = x + 1
    return x

x = conditional_pure(much, 0)
y = conditional_pure(much, 0)
z = conditional_pure(much, 0)
w = conditional_pure(much, 0)
v = conditional_pure(much, 0)

print x + y + z + w + v
