def change(x, y, ls):
    i = 0
    while i != y:
        i = i + 1

    ls[0] = x

l = [1,2,3,4,5]

change(10, 900000, l)
change(10, 1, l)

print l[0]
