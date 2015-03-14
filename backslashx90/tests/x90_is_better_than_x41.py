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
    def my_map(idx):
        return [] if idx == length else [f(lst[idx])] + my_map(idx+1)
    return my_map(0)

def my_range(x):
    return [] if x == 0 else my_range(x+-1) + [x]

def foldl(f, init, lst, l):
    def foldl_p(f, init, lst, idx, length):
        return init if idx == length else foldl_p(f, f(init, lst[idx]), lst, idx+1, length)
    return foldl_p(f, init, lst, 0, l)

def mul(x, y):
    return 0 if x == 0 or y == 0 else x + mul(x, y +- 1)

def curry_mul(x):
    return (lambda y: mul(x,y))

def square(x):
    return curry_mul(x)(x)

def super_curry2(x):
    return super_curry if not even(x) else x

def super_curry(x):
    return super_curry2 if even(x) else x

length_of_davis = 26
davis = my_range(length_of_davis)

print curry_mul(2)(3)

cdavis = my_map(collatz, davis, length_of_davis)
print cdavis

ddavis = my_map(curry_mul(2), cdavis, length_of_davis)
print ddavis

sdavis = my_map(square, ddavis, length_of_davis)
print sdavis

sum_davis = (lambda l: foldl(lambda x,y: x+y, 0, l, length_of_davis))(sdavis)
print sum_davis

leslie = [square, curry_mul(2), curry_mul(3), lambda x: x + 2]
better_leslie = my_map(lambda f: f(3), leslie, 4)

print better_leslie

print super_curry(0)(1)(2)(1)(4)(7)(2)(5)(8)(11)(12)(15)(18)(91)(4)(3)(387)
