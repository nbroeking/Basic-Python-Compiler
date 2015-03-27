def fib(x):
    return 1 if (x == 0 or x == 1) else fib(x+-1) + fib(x+-2)

print fib(6)

def fib(n):
    def fib(prev, length, n):
        def fib2(prev, length, n):
            next = prev[length+-1] + prev[length+-2]
            newlist = prev + [next]
            return fib(newlist, length+1, n+-1)
            
        return prev if n == 0 else fib2(prev, length, n)
    return fib([1,1], 2, n+-2)

print fib(43)
