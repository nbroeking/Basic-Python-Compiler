def tricky0(y):
    v = 2
    def tricky1():
        return v + y
    return tricky1

print tricky0(6)()
