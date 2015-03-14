davis = [1,2]
print ([lambda x: x + [input()] + davis, lambda y: y + davis + [input()]])[input()]([3,4])

def buddy_holly(x):
    print x
    return [] if x == 0 else [x] + buddy_holly(x+-1)

buddy_holly(1)
