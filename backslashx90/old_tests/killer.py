class x:
    class y:
        w = 2

        def __init__(self):
            self.x = 1

# x = MkClass
# $0$ = MkClass
# set_attr(x, "y", $0$)
# set_attr(get_attr(x, "y"), "w", 2)

print x.y.w
print x.y().x
