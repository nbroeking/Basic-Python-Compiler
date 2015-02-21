# AsmTree
#
#

from AsmTypes import *


class Condition:
    def __init__(self, jmpstmt, pretty_name): # : string, string
        self.pretty_name = pretty_name
        self.jmpstmt = jmpstmt

    def __str__(self):
        return self.pretty_name

ZERO = Condition("jz", "zero")
NOT_ZERO = Condition("jnz", "not zero")
GREATER_THAN = Condition("jg", "greater")
LESS_THAN = Condition("jl", "less")
GREATER_THAN_EQ = Condition("jge", "greater eq")
LESS_THAN_EQ = Condition("lte", "less eq")

if_count = 0
class If:
    def __init__(self, cond, then_stmts, else_stmts):
        global if_count 

        self.cond = cond # :: Condition
        self.else_stmts = [Jz(".Lthen%d" % if_count)] + else_stmts + [Jmp(".Lendif%d" % if_count)]
        self.then_stmts = [Label(".Lthen%d" % if_count)] + then_stmts + [Label(".Lendif%d" % if_count)]

        if_count += 1

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()
    def _to_str(self):
        return "if %s { \n   %s \n} else { \n   %s \n}" % (self.cond, "\n   ".join( map(str, self.then_stmts) ), "\n   ".join( map(str, self.else_stmts) ))

#Mov Object
class Movl:
    def __init__(self, src, dest):
        if not isinstance(src, AsmVar) or not isinstance(dest, AsmVar):
            raise Exception()

        self.src = src
        self.dest = dest

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.src = f(self.src)
        self.dest = f(self.dest)

    def _to_str(self):
        return "movl %s, %s" % (self.src, self.dest)
#Add
class Label:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception()

        self.name = name

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        pass

    def _to_str(self):
        return "%s:" % (self.name)

#Add
class Jmp:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception()

        self.name = name

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        pass

    def _to_str(self):
        return "jmp %s" % (self.name)

#Add
class Jz:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception()

        self.name = name

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        pass

    def _to_str(self):
        return "jz %s" % (self.name)

#Add
class Jnz:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception()

        self.name = name

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        pass

    def _to_str(self):
        return "jnz %s" % (self.name)

#Add
class Addl:
    def __init__(self, lhs, rhs):
        if not isinstance(lhs, AsmVar) or not isinstance(rhs, AsmVar):
            raise Exception()

        self.lhs = lhs
        self.rhs = rhs

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.rhs = f(self.rhs)
        self.lhs = f(self.lhs)

    def _to_str(self):
        return "addl %s, %s" % (self.lhs, self.rhs)

#Add
class Andl:
    def __init__(self, lhs, rhs):
        if not isinstance(lhs, AsmVar) or not isinstance(rhs, AsmVar):
            raise Exception()

        self.lhs = lhs
        self.rhs = rhs

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.rhs = f(self.rhs)
        self.lhs = f(self.lhs)

    def _to_str(self):
        return "andl %s, %s" % (self.lhs, self.rhs)

class Cmpl:
    def __init__(self, lhs, rhs):
        if not isinstance(lhs, AsmVar) or not isinstance(rhs, AsmVar):
            raise Exception()

        self.lhs = lhs
        self.rhs = rhs

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.rhs = f(self.rhs)
        self.lhs = f(self.lhs)

    def _to_str(self):
        return "cmpl %s, %s" % (self.lhs, self.rhs)

#Neg 
class Neg:
    def __init__(self, value):
        if not isinstance(value, AsmVar):
            raise Exception()
        self.val = value

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()
    
    def _to_str(self):
        return "negl %s " % ( self.val )

    def map_vars(self, f): # apply function to all vars
        self.val = f(self.val)

class Testl:
    def __init__(self, lhs, rhs):
        if not isinstance(lhs, AsmVar) and not isinstance(rhs, AsmVar):
            raise Exception()
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()
    
    def _to_str(self):
        return "testl %s, %s " % ( self.lhs, self.rhs )

    def map_vars(self, f): # apply function to all vars
        self.rhs = f(self.rhs)
        self.lhs = f(self.lhs)

#Push
class Push:
    def __init__(self, value):
        if not isinstance(value, AsmVar):
            raise Exception()
        self.val = value

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

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
    def __repr__(self): return self._to_str()

    def _to_str(self):
        return "popl %s" %(self.val)

    def map_vars(self, f): # apply function to all vars
        self.val = f(self.val)

class Call:
    def __init__(self, name):
        self.name = name

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

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
    def __repr__(self): return self._to_str()

    def _to_str(self):
        return "subl %s, %s" % (self.lhs, self.rhs)

    def map_vars(self, f): # apply function to all vars
        self.lhs = f(self.lhs)
        self.rhs = f(self.rhs)

class Ret:
    def __init(self):
        pass

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def _to_str(self):
        return "ret"
