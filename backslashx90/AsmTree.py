# AsmTree
#
#

#Mov Object
class Movl:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        
    def _to_str(self):
        return "movl %s = %s" % (self.src, self.dest)

#Add
class Addl:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def _to_str(self):
        return "%s += %s" % (self.rhs, self lhs)

class Neg:
    def __init__(self, value):
        self.val = value
    
    def _to_str(self):
        return "- %s " % ( self.val )

class Push:
    def __init__(self, value):
        self.val = value

    def _to_str(self):
        return "push %s" % (self.val)

class Pop:
    def __init__(self, value):
        self.val = value

    def _to_str(self):
        return "pop %s" %(self.val)

class Call:
    def __init__(self, name):
        self.name = name

    def _to_str(self):
        return "call %s" % (self.name)

class Subl:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def _to_str(self):
        return "%s -= %s" % (self.lhs, self.rhs)


