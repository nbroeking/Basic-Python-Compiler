
davis_is_glad_get = lambda x: davis_is_glad[x]

def fn0(x):
    print 0
    return [3, 5] if x == 3 else [1 if x == 0 else 2, x + 1]
    
def fn1(x):
    print 1
    return [2, x] if x == 0 else [x +- 1, x + x]

def fn2(x):
    print 2
    return [4, lambda x: x+-3] if x == 0 else [1, x +- x]

def fn4(f):
    print 4
    return [f(10), f(3)]

def fn7(x):
    hanger = [68, 97, 118, 105, 115, 32, 105, 115, 32, 72, 97, 110, 103, 114, 121, 33]
    print hanger
    return hanger

def fn68(x):
    return [0, fn0(3)[0]]

davis_is_glad = {
    0: fn0, 1: fn1, 2: fn2, 3: 0,
    4: fn4, 7: fn7, 68: fn68
}

def iterate(x, a):
    def iterate2(x, a):
        lst = davis_is_glad_get(x)(a)
        newx = lst[0]
        newa = lst[1]
        return iterate(newx, newa)

    return 0 if davis_is_glad_get(x) == 0 else iterate2(x, a)

print iterate(0,0)
