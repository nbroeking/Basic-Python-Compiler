def my_map(f, lst, size):
    i = 0
    retlst = []
    while i != size:
        retlst = retlst + [f(lst[i])]
        i = i + 1
    return retlst

def p1(x):
    print x
    return x + 1

print my_map(p1, [1,2,3,4,5,6], 6)
        

