class y:
    x = 5
    def __init__(self):
        self.y = 3

    def printer(self):
        print y.x + self.y

yes = y()
yes.printer()
