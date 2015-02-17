# AsmTree
#
#

from AsmTypes import *

#Mov Object
class Movl:
    def __init__(self, src, dest):
        if not isinstance(src, AsmVar) or not isinstance(dest, AsmVar):
            raise Exception()

        self.src = src
        self.dest = dest

    def __str__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.src = f(self.src)
        self.dest = f(self.dest)

    def _to_str(self):
        return "movl %s, %s" % (self.src, self.dest)

#Add
class Addl:
    def __init__(self, lhs, rhs):
        if not isinstance(lhs, AsmVar) or not isinstance(rhs, AsmVar):
            raise Exception()

        self.lhs = lhs
        self.rhs = rhs

    def __str__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.rhs = f(self.rhs)
        self.lhs = f(self.lhs)

    def _to_str(self):
        return "addl %s, %s" % (self.lhs, self.rhs)
#Neg 
class Neg:
    def __init__(self, value):
        if not isinstance(value, AsmVar):
            raise Exception()
        self.val = value

    def __str__(self): return self._to_str()
    
    def _to_str(self):
        return "negl %s " % ( self.val )

    def map_vars(self, f): # apply function to all vars
        self.val = f(self.val)
#Push
class Push:
    def __init__(self, value):
        if not isinstance(value, AsmVar):
            raise Exception()
        self.val = value

    def __str__(self): return self._to_str()

    def _to_str(self):
        return "pushl %s" % (self.val)

    def map_vars(self, f): # apply function to all vars
        self.val = f(self.val)

class Pop:
    def __init__(self, value):
        if not isinstance(value, AsmVar):
            raise Exception()
        self.val = value

    def __str__(self): return self._to_str()

    def _to_str(self):
        return "popl %s" %(self.val)

    def map_vars(self, f): # apply function to all vars
        self.val = f(self.val)

class Call:
    def __init__(self, name):
        self.name = name

    def __str__(self): return self._to_str()

    def _to_str(self):
        return "call %s" % (self.name)


    def map_vars(self, f): # apply function to all vars
        pass

class Subl:
    def __init__(self, lhs, rhs):
        if not isinstance(lhs, AsmVar) or not isinstance(rhs, AsmVar):
            raise Exception()
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self): return self._to_str()

    def _to_str(self):
        return "subl %s, %s" % (self.lhs, self.rhs)

    def map_vars(self, f): # apply function to all vars
        self.lhs = f(self.lhs)
        self.rhs = f(self.rhs)

class Ret:
    def __init(self):
        pass

    def __str__(self): return self._to_str()

    def _to_str(self):
        return "ret"
