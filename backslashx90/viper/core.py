# This mudle contains the AST for the core intermediate language
# this is the language the first stage of translation goes to.

# the assignment operator. The right hand side must be a base
class WTFException(Exception):
    def __init__(self, s):
            super(self, Exception).__init__(s)

class CoreNode:
    def _to_str(self):
        return ""
    def __str__(self):
        return self._to_str()

class Assign(CoreNode):
    def __init__(self, name, rhs):
        self.rhs = rhs
        self.name = name
        self.children = [self.rhs]

    def _to_str(self):
        return "%s = %s" % (self.name, self.rhs._to_str())

# a constant value
class Const(CoreNode):
    def __init__(self, raw):
        self.raw = raw
        self.children = []

    def _to_str(self):
        return "%s" % (self.raw)

class PyConst(CoreNode):
    def __init__(self, raw):
        self.raw = raw
        self.children = []

    def _to_str(self):
        return "p(%s)" % self.raw

# a variable name
class Name(CoreNode):
    def __init__(self, name):
        self.name = name
        self.children = []

    def _to_str(self):
        return "$%s" % (self.name)

# call a function with arguments
class CallFunc(CoreNode):
    def __init__(self, lhs, args):
        self.lhs = lhs
        self.args = args
        self.children = list(self.args)

    def _to_str(self):
        return self.lhs._to_str() + "(" + ",".join([i._to_str() for i in self.args]) + ")"

class Deref(CoreNode):
    def __init__(self, arg, offset):
        self.arg = arg
        self.offset = offset

    def _to_str(self):
        return "0x%x(%s)" % (self.offset, self.arg)

class Neg(CoreNode):
    def __init__(self, rhs):
        self.rhs = rhs;
        self.children = [rhs];

    def _to_str(self):
        return "- " + self.rhs._to_str()

class Print(CoreNode):
    def __init__(self, rhs):
        self.rhs = rhs
        self.children = [self.rhs]

    def _to_str(self):
        return "print " + self.rhs._to_str()
        

# an addition. In this step, an addition may only contain Const's and
# Name's as the possible lhs's and rhs's. No sub additions.
class Add(CoreNode):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.children = [self.lhs,self.rhs]

    def _to_str(self):
        return "(%s + %s)" % (self.lhs._to_str(), self.rhs._to_str())

class PyAdd(CoreNode):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.children = [self.lhs, self.rhs]

    def _to_str(self):
        return "(%s p+ %s)" % (self.lhs, self.rhs)

# same goes for the following
class Mul(CoreNode):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.children = [self.lhs,self.rhs]

    def _to_str(self):
        return "(%s * %s)" % (self.lhs._to_str(), self.rhs._to_str())

class List(CoreNode):
    def __init__(self, elements):
        self.elems = elements

    def _to_str(self):
        tmp = [str(x) for x in self.elems]
        return "[%s]" % (",".join(tmp))
    def __str__(self):
        return self._to_str()

class Div(CoreNode):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.children = [self.lhs,self.rhs]

    def _to_str(self):
        return "(%s / %s)" % (self.lhs._to_str(), self.rhs._to_str())