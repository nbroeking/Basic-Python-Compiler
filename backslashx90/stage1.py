# this module is the spec of the intermediate
# language ast that implements the spec for
# the current project.

import compiler.ast as pyast
import compiler as comp
import core
import sys

def is_base(pyst):
    return isinstance(pyst, pyast.Const) or \
           isinstance(pyst, pyast.Name)


def base_cov(pyst):
    if isinstance(pyst, pyast.Const):
        return core.Const(pyst.getChildren()[0])
    if isinstance(pyst, pyast.Name):
        return core.Name(pyst.getChildren()[0])


class Stage1:
    def __init__(self):
        self.tempcount = 0
        self.buffer = []

    def tmpvar(self):
        tmp = "$%d$" % self.tempcount
        self.tempcount += 1
        return tmp

    def trans(self, pyst, lhs, rhs):
        return \
            { pyast.Add: core.Add,
              pyast.Div: core.Div,
              pyast.Mul: core.Mul
            }[pyst.__class__](lhs, rhs)

    def loose_flatten_op(self, pyst):
        lhs, rhs = pyst.asList()
        lhs_, rhs_ = base_cov(lhs), base_cov(rhs)

        if is_base(lhs) and is_base(rhs):
            var = self.tmpvar()
            self.buffer += [core.Assign(var, self.trans(pyst, lhs_, rhs_))];
            return var

        else:
            if not is_base(rhs):
                var = self.loose_flatten(rhs)
                return self.loose_flatten(pyst.__class__((lhs, pyast.Name(var))))

            else:
                var = self.loose_flatten(lhs)
                return self.loose_flatten(pyst.__class__((pyast.Name(var), rhs)))

    def loose_flatten_func(self, pyst):
        lst = pyst.getChildNodes();
        lhs = lst[0]
        args = lst[1:]

        if is_base(lhs) and all([is_base(i) for i in args]):
            var = self.tmpvar()
            self.buffer += [core.Assign(var, core.CallFunc(base_cov(lhs), [base_cov(i) for i in args]))]
            return var

        if not is_base(lhs):
            var = self.loose_flatten(lhs)
            return self.loose_flatten(pyast.CallFunc(pyast.Name(var), args, None, None))

        for i in range(len(args)):
            if not is_base(args[i]):
                var = self.loose_flatten(args[i])
                argsp = args[0:i] + (pyast.Name(var),) + args[i+1:]
                return self.loose_flatten(pyast.CallFunc(lhs, argsp, None, None))

        raise Exception("Why did this not pass the first check?")
        
    def loose_flatten(self, pyst):
        if is_base(pyst):
            return None

        if isinstance(pyst, pyast.Add) or \
           isinstance(pyst, pyast.Mul) or \
           isinstance(pyst, pyast.Div):

            return self.loose_flatten_op(pyst)

        if isinstance(pyst, pyast.CallFunc):
            return self.loose_flatten_func(pyst)

        else:
            raise Exception('Unexpected in loose flatten ' + pyst.__class__.__name__)

    def flatten_assign(self, pyst):
        if isinstance(pyst, pyast.Assign):
            var = self.loose_flatten(pyst.getChildren()[1])
            if var is None:
                rhs = base_cov(pyst.getChildren()[1])
            else:
                rhs = core.Name(var)
            self.buffer += [core.Assign(pyst.getChildren()[0].getChildren()[0], rhs)]
        else:
            raise Exception("Expected an Assign instance")

    def flatten(self, pyst):
        if isinstance(pyst, pyast.Assign):
            self.flatten_assign(pyst)
        elif isinstance(pyst, pyast.Module):
            self.flatten(pyst.getChildren()[1])
        elif isinstance(pyst, pyast.Stmt):
            for i in pyst.getChildren():
                self.flatten(i)
        elif isinstance(pyst, pyast.Discard):
            self.flatten(pyst.getChildren()[0])
        elif isinstance(pyst, pyast.Add):
            self.loose_flatten(pyst)
        else:
            raise Exception("Unexpected " + pyst.__class__.__name__)

        return self.buffer

def flatten(ast):
    sg1 = Stage1()
    return sg1.flatten(ast)

def print_core_ast( core ): # core : [AST]
    return "\n".join([i._to_str() for i in core])
