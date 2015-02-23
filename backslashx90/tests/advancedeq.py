x = 1
y = 2
z = [1,2,4,5,6,7]

if x == y:
    print 90
else:
    print 78

u = x + z if x == y else 1
print u

p = 1 if x == 1 == True == True else x + 2
print p

o = 56 if [1,2,3,4,5] == [1,2,3,4,5] else 78
print o

xx = [67,68,69]
yy = xx
if xx == yy:
    print 987

if yy == [1] == xx + 2:
    print 0
else:
    print 1
