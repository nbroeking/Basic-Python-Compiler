def fib(x):
    return 1 if (x == 0 or x == 1) else fib(x+-1) + fib(x+-2)

print fib(6)
