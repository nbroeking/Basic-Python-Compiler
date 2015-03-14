def test(x):
    even = lambda z: True if z == k else odd(z+-1)
    odd = lambda z: False if z == k else even(z+-1)

    k = 0
    return even(x)

print test(4)
