
def foldl_p(f, init, lst, idx, length):
    return init if idx == length else foldl_p(f, f(init, lst[idx]), lst, idx+1, length)

def foldl(f, init, lst, l):
    return foldl_p(f, init, lst, 0, l)

def my_sum(lst, length):
    return foldl(lambda x, y: x + y, 0, lst, length)

def mul(x, y):
    return 0 if x == 0 or y == 0 else y + mul(x+-1, y)

def my_map(f, lst, length):
    def map_p(f, lst, idx, length):
        return [] if idx == length else [f(lst[idx])] + map_p(f, lst, idx+1, length)
    return map_p(f, lst, 0, length)

mylist = [1,2,3,4,5]
print my_sum( my_map(lambda x: x + 1, mylist, 5), 5 )
