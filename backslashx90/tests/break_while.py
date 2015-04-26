
def pure():
    i = 0
    while i != 1000000:
        i = i + 1
    return i

def pure2():
    r = pure()
    return 5

x = 5
x = pure()

while x != 5:
    print 0
    x = pure2()
