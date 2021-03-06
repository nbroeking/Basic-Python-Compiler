def my_map(f, lst, length):
    def map_p(f, lst, idx, length):
        return [] if idx == length else [f(lst[idx])] + map_p(f, lst, idx+1, length)
    return map_p(f, lst, 0, length)

leslie = [1,2,3,4]

def mul(x, y):
    return 0 if x == 0 or y == 0 else x + mul(x, y +- 1)

new_leslie = my_map(lambda x: [mul(x,x)] + leslie, leslie, 4)
print new_leslie
