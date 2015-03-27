def pure(l):
    x = l.copy()
    x.append(5)
    return x

def impure(l):
    l.append(5)
    return l
