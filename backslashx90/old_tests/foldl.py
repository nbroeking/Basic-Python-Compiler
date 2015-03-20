
def foldl(f, init, lst, l):
    def foldl_p(f, init, lst, idx, length):
        return init if idx == length else foldl_p(f, f(init, lst[idx]), lst, idx+1, length)
    return foldl_p(f, init, lst, 0, l)

def my_sum(lst, length):
    return foldl(lambda x, y: x + y, 0, lst, length)

mylist = [1,2,3,4,5]
print my_sum(mylist, 5)
