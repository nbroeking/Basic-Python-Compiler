# x > y
def is_greater(x, y):
    return False if x == y else (True if y == 0 else False if x == 0 else is_greater(x+-1,y+-1))

def mfilter(f, lst, length):
    def mfilter(idx):
        return [] if idx == length else (([lst[idx]] if f(lst[idx]) else []) + mfilter(idx+1))
    return mfilter(0)
    
print is_greater(5,4)
print is_greater(8,2)
print is_greater(2,8)

print mfilter(lambda x: x == 2, [1,2,3,2], 4)

x = [3,4,5563,2341,7,8,43,050,342,234,103,131,1313,13,1231,131,03,23,123,134,2]
