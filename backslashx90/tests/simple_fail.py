def tricky0(y):
    def tricky1():
        return y
    return tricky1

print tricky0(6)()
