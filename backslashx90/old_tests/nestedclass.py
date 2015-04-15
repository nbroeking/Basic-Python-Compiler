class x:
    class y:
        x = 4
        def printer(self):
            print x.y.x

    def __init__(self):
        self.j = x.y()

    def printer(self):
        self.j.printer()

n = x()

n.printer()


