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
while_count = 0
class While:
    def __init__(self, cond, then_stmts):
        global while_count 
        
        self.cond = [
            Comment("Start while loop"),
            Label(".Lstart_while%d" % while_count),
            Comment("While loop condition")] + cond + [Jmp(".Lend_while%d" % while_count, "jz")] # :: Condition
        self.then_stmts = then_stmts + [Jmp(".Lstart_while%d" % while_count)] + [Comment("End While"), Label(".Lend_while%d" % while_count)]

        while_count += 1

    def map_vars(self, f):
        for i in self.cond:
            i.map_vars(f)
        for i in self.then_stmts:
            i.map_vars(f)

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()
    def _to_str(self):
        return "while (%s) { \n   %s \n} " % ("\n    ".join(map(str,self.cond)), "\n   ".join( map(str, self.then_stmts) ))


class If:
    def __init__(self, cond, then_stmts, else_stmts):
        global if_count 

        self.cond = cond # :: Condition
        self.else_stmts = [Jmp(".Lthen%d" % if_count, cond.jmpstmt)] + else_stmts + [Jmp(".Lendif%d" % if_count)]
        self.then_stmts = [Label(".Lthen%d" % if_count)] + then_stmts + [Label(".Lendif%d" % if_count)]

        if_count += 1

    def map_vars(self, f):
        for i in self.then_stmts:
            i.map_vars(f)
        for i in self.else_stmts:
            i.map_vars(f)

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()
    def _to_str(self):
        return "if %s { \n   %s \n} else { \n   %s \n}" % (self.cond, "\n   ".join( map(str, self.then_stmts) ), "\n   ".join( map(str, self.else_stmts) ))

#Mov Object
class Movl:
    def __init__(self, src, dest):
        if not isinstance(src, AsmVar) or not isinstance(dest, AsmVar):
            raise Exception()

        self.lhs = src
        self.rhs = dest

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.lhs = f(self.lhs)
        self.rhs = f(self.rhs)

    def _to_str(self):
        return "movl %s, %s" % (self.lhs, self.rhs)

class Leal:
    def __init__(self, src, dest):
        if not isinstance(src, AsmVar) or not isinstance(dest, AsmVar):
            raise Exception()

        self.lhs = src
        self.rhs = dest

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.lhs = f(self.lhs)
        self.rhs = f(self.rhs)

    def _to_str(self):
        return "leal %s, %s" % (self.lhs, self.rhs)

class Cmovzl:
    def __init__(self, src, dest):
        if not isinstance(src, AsmVar) or not isinstance(dest, AsmVar):
            raise Exception()

        self.lhs = src
        self.rhs = dest

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        self.lhs = f(self.lhs)
        self.rhs = f(self.rhs)

    def _to_str(self):
        return "cmovzl %s, %s" % (self.lhs, self.rhs)

class Comment:
    def __init__(self, comment):
        self.comment = comment

    def __str__(self): return self._to_str()

    def _to_str(self):
        return "/* %s */" %self.comment

    def map_vars(self, _):
        pass

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
    def __init__(self, name, asm="jmp"):
        if not isinstance(name, str):
            raise Exception()

        self.name = name
        self.asm = asm

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def map_vars(self, f): # apply function to all vars
        pass

    def _to_str(self):
        return "%s %s" % (self.asm, self.name)

#Add

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

class Shll:
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
        return "shll %s, %s" % (self.lhs, self.rhs)

class Shrl:
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
        return "shrl %s, %s" % (self.lhs, self.rhs)

class Xorl:
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
        return "xorl %s, %s" % (self.lhs, self.rhs)

class Orl:
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
        return "orl %s, %s" % (self.lhs, self.rhs)

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

class CallStar:
    def __init__(self, name):
        self.name = name
        self.val = name

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def _to_str(self):
        return "call *%s" % (self.name)

    def map_vars(self, f): # apply function to all vars
        self.name = f(self.name)
        self.val = f(self.val)

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

class Raw:
    def __init__(self, string):
        self.string = string

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def _to_str(self):
        return self.string

class Leave:
    def __init(self):
        pass

    def __str__(self): return self._to_str()
    def __repr__(self): return self._to_str()

    def _to_str(self):
        return "leave"
