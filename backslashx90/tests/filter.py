def mfilter(f, lst, length):
    def mfilter(idx):
        return [] if idx == length else (([lst[idx]] if f(lst[idx]) else []) + mfilter(idx+1))
    return mfilter(0)

print mfilter(lambda x: x == 2, [1,2,3,2], 4)
