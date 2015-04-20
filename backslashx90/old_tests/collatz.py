def even(x):
    return True if x == 0 else (False if x == 1 else even(x+-2))

def div2(x):
    return 0 if x == 0 or x == 1 else 1 + div2(x+-2)

def mul3p1(x):
    return x + x + x + 1

def collatz(x):

    return 0 if x == 1 else \
            1+collatz(div2(x)) if even(x) else 1+collatz(mul3p1(x))

def my_map(f, lst, length):
    def map_p(f, lst, idx, length):
        return [] if idx == length else [f(lst[idx])] + map_p(f, lst, idx+1, length)
    return map_p(f, lst, 0, length)

def my_range(x):
    return [] if x == 0 else my_range(x+-1) + [x]

davis = my_range(12)

print my_map(collatz, davis, 12)
