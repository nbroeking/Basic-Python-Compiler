# This mudle contains the AST for the core intermediate language
# this is the language the first stage of translation goes to.

# the assignment operator. The right hand side must be a base
class WTFException(Exception):
    def __init__(self, s):
            super(self, Exception).__init__(s)

class Assign:
    def __init__(self, name, rhs):
        self.rhs = rhs
        self.name = name
        self.children = [self.rhs]

    def _to_str(self):
        return "%s = %s" % (self.name, self.rhs._to_str())

# a constant value
class Const:
    def __init__(self, raw):
        self.raw = raw
        self.children = []

    def _to_str(self):
        return "%s" % (self.raw)

# a variable name
class Name:
    def __init__(self, name):
        self.name = name
        self.children = []

    def _to_str(self):
        return "$%s" % (self.name)

# call a function with arguments
class CallFunc:
    def __init__(self, lhs, args):
        self.lhs = lhs
        self.args = args
        self.children = list(self.args)

    def _to_str(self):
        return self.lhs._to_str() + "(" + ",".join([i._to_str() for i in self.args]) + ")"

class Neg:
    def __init__(self, rhs):
        self.rhs = rhs;
        self.children = [rhs];

    def _to_str(self):
        return "- " + self.rhs._to_str()

class Print:
    def __init__(self, rhs):
        self.rhs = rhs
        self.children = [self.rhs]

    def _to_str(self):
        return "print " + self.rhs._to_str()
        

# an addition. In this step, an addition may only contain Const's and
# Name's as the possible lhs's and rhs's. No sub additions.
class Add:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.children = [self.lhs,self.rhs]

    def _to_str(self):
        return "(%s + %s)" % (self.lhs._to_str(), self.rhs._to_str())

# same goes for the following

class Mul:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.children = [self.lhs,self.rhs]

    def _to_str(self):
        return "(%s * %s)" % (self.lhs._to_str(), self.rhs._to_str())

class Div:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.children = [self.lhs,self.rhs]

    def _to_str(self):
        return "(%s / %s)" % (self.lhs._to_str(), self.rhs._to_str())
