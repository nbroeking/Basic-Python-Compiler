# x > y
def is_greater(x):
    def is_greater2(y):
        return False if x == y else (True if y == 0 else False if x == 0 else is_greater(x+-1)(y+-1))
    return is_greater2

def mfilter(f, lst, idx, length):
    def mfilter2(idx):
        tail = mfilter(idx + 1)
        size = tail[0]
        tail = tail[1]

        return [size+1,[lst[idx]]+tail] if f(lst[idx]) else [size, tail]

    def mfilter(idx):
        return [0,[]] if idx == length else mfilter2(idx)

    return mfilter(idx)

def compose(f, g):
    return lambda x: f(g(x))

def notf(x):
    return not x

def quick_sort(lst, length):
    def quick_sort2(lst, length):
        piv = lst[0]
        ltl = mfilter(is_greater(lst[0]), lst, 1, length)
        gtl = mfilter(compose(notf, is_greater(lst[0])), lst, 1, length)
    
        lt_size = ltl[0]
        lt = ltl[1]
    
        gt_size = gtl[0]
        gt = gtl[1]
    
        ltn = quick_sort(lt, lt_size)
        gtn = quick_sort(gt, gt_size)
    
        return ltn + [piv] + gtn

    return [] if length == 0 else quick_sort2(lst, length)

    
x_len = 255
x = [168, 92, 202, 169, 237, 248, 238, 47, 163, 252, 254, 123, 70, 45, 191, 132,
     36, 131, 51, 157, 173, 186, 33, 196, 145, 120, 125, 43, 73, 78, 21, 0, 4,
     112, 32, 129, 145, 128, 55, 24, 24, 167, 112, 67, 149, 210, 63, 3, 10, 149,
     251, 149, 59, 2, 16, 137, 227, 208, 137, 91, 146, 146, 220, 181, 151, 9, 177,
     10, 49, 127, 162, 141, 231, 96, 229, 23, 194, 135, 241, 148, 116, 155, 99, 118,
     77, 191, 193, 65, 17, 181, 145, 242, 73, 70, 20, 65, 42, 156, 94, 65, 196, 141,
     22, 50, 61, 118, 184, 47, 112, 200, 102, 154, 147, 33, 89, 185, 71, 39, 6, 146,
     48, 80, 112, 106, 223, 71, 58, 1, 129, 129, 154, 70, 234, 51, 119, 142, 206, 65,
     122, 205, 133, 170, 107, 162, 69, 223, 239, 89, 239, 26, 165, 210, 156, 208, 69,
     254, 98, 104, 16, 131, 236, 145, 13, 254, 44, 88, 55, 220, 87, 210, 141, 33, 48,
     223, 128, 68, 8, 125, 224, 203, 216, 104, 78, 200, 118, 19, 17, 245, 190, 238, 166,
     172, 250, 100, 119, 243, 18, 154, 2, 236, 236, 17, 5, 181, 190, 14, 69, 81, 134, 242,
     52, 175, 143, 118, 111, 164, 148, 138, 187, 20, 213, 25, 193, 239, 15, 43, 250, 55, 18,
     147, 29, 205, 138, 24, 62, 53, 47, 90, 194, 77, 15, 42, 74, 25, 226, 155, 236, 52, 150,
     114, 195, 190, 199, 220, 25]
print x
print quick_sort(x, x_len)
