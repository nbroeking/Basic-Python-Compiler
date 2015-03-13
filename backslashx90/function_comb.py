import compiler.ast as ast
import printer

try:
    from viper.AsmTree import *
except:
    from AsmTree import *

# this module is responsible for "combing" out functions
# and making the main code into it's own main function

# This will take a python ast and return a list of new
# python ast's; one for each function found.

preamble = [
      Push(var_raw("%ebp"))
    , Movl(var_raw("%esp"), var_raw("%ebp"))
    , Subl(var_const("12"), var_raw("%esp"))
    , Movl(var_raw("%ebx"), var_raw_mem("(%esp)"))
    , Movl(var_raw("%esi"), var_raw_mem("4(%esp)"))
    , Movl(var_raw("%edi"), var_raw_mem("8(%esp)"))
]

postamble = [
      Movl(var_raw_mem("(%esp)" ), var_raw("%ebx"))
    , Movl(var_raw_mem("4(%esp)"), var_raw("%esi"))
    , Movl(var_raw_mem("8(%esp)"), var_raw("%edi"))
    , Addl(var_const("12"), var_raw("%esp"))
    , Leave()
    , Ret()
]

class DefinedFunction:
    # name : string -- name of the function
    # args : list<string> -- argument list
    # closure : map<string, int> -- map of variable name to their offset
    # pyast : the ast in this function
    def __init__(self, name, args, closure, pyast, children):
        self.name = name
        self.args = args
        self.closure = closure
        self.pyast = pyast
        self.children = children # [DefinedFunction]

    def get_ast(self):
        return self.pyast

    def set_ast(self, nast):
        self.pyast = nast

    def __str__(self):
        return "%s(%s) { %s } (closure: %s)" % (self.name, ",".join(self.args), self.pyast, self.closure)

    def build_final_asm_tree(self):
        return [
            Raw(""),
            Raw(".globl %s" % self.name),
            Raw(".type %s,@function" % self.name),
            Label("%s" % self.name),
        ] + preamble + self.pyast + [Label(".%s_ret" % self.name)] + postamble
        

# there are two stages to breaking out the functions,
# the first is to find them, break them out, and
# then we need to analyze the unbound variables to calculate
# the closures
#
# pyst : PythonAST -- the ast of the entire program
# returns : list<DefinedFunction> -- a list of functions which have been defined
def preprocess_functions(pyst):
    if isinstance(pyst, ast.Module):
        # for modules, just strip it
        return preprocess_functions(pyst.getChildren()[1])

    # Now we probably have statements
    if isinstance(pyst, ast.Stmt):
        # fnlst : [(Function, [Function])] | lhs = parent & rhs = children
        (newast, fnlst) = loose_preprocess_functions(pyst)

        fn = ast.Function(None, mangle("","main"), [], [], 0, None, newast)
        rootfn = (fn, fnlst)

        defn = to_defined_function(rootfn) # return DefinedFunction
        return flatten_function_tree(defn)

    raise Exception("Unexpected " + str(pyst.__class__) + " in preprocess functions")

def flatten_function_tree(rootfn):
    tot_ret = []
    for i in rootfn.children:
        tot_ret += flatten_function_tree(i)
    tot_ret.append( rootfn )
    return tot_ret
        

def set_to_map(s):
    md = {}
    v = 0
    for i in s:
        md[i] = v
        v += 1
    return md
#
# Converts a python ast Function to a DefinedFunction
# by calculating the closure
def to_defined_function(function_p):
    (parent, children) = function_p

    new_children = [to_defined_function(i) for i in children]

    (_, name, args, _, _, stmts) = parent.getChildren()
    free_vars = get_free_vars(stmts)
    for child in new_children:
        free_vars |= set(child.closure.keys())

    # subtract out the args given
    free_vars -= set(args) 

    return DefinedFunction(name, args, set_to_map(free_vars), stmts, new_children)

def mangle(a_name, name_p):
    return "x90_" + a_name + "_" + name_p


# return a set of the free vars in 
# the function
def get_free_vars(pyast):

    # Start with a list of all the name referenced and
    # then remove all of the one which are assigned in
    # the function
    def loose_get_free_vars(pyast):
        if isinstance(pyast, ast.Name):
            return (set(), set([pyast.getChildren()[0]]))
    
        elif isinstance(pyast, ast.Assign):
            if isinstance(pyast.getChildren()[0], ast.AssName):
                return (set([pyast.getChildren()[0].getChildren()[0]]), set())
            else:
                return (set(),set())
    
        else:
            total_ref = set()
            total_assign = set()
    
            for i in pyast.getChildNodes():
                (assign, ref) = loose_get_free_vars(i)
                total_ref |= ref
                total_assign |= assign
    
            return (total_assign, total_ref)

    (assign, ref) = loose_get_free_vars(pyast)
    print "(ASSIGN, REF)",(assign,ref)
    return (ref - assign - set(["True", "False"]))

# this needs to be a separate class so that
# way we can intercept and build the closure
# during the instruction stage
class FnName:
    def __init__(self, name):
        self.name = name

    def getChildNodes(self):
        return []

    def _to_str(self):
        return "fn(%s)" % self.name

    def __str__(self):
        return self._to_str()

    def __repr__(self):
        return self._to_str()

# Extracts lambdas and def's from the abstract syntax
# tree. This function is tricky; it returns a tuple
# of (PyAst, [PyAst]) where the first PyAst is the new
# ast (modified from lambdas to identifiers) and the list
# is an array of function ast nodes

nonce = 0 # because FML
def loose_preprocess_functions(pyast,a_name="main"):
    global nonce
    # list of ASTs of the functions to pull out
    functionlist = []

    if isinstance(pyast, ast.Stmt):
        retlist = []

        # for a statement, we can parse all the
        # children
        stmtlst = pyast.getChildren()
        for i in stmtlst:
            # if the node is a function, then
            # append it to the list, otherwise,
            # append any functions found in the sub
            # tree
            if isinstance(i, ast.Function):
                (_, name, args, _, _, stmts) = i.getChildren()

                mname = mangle(a_name, name)
                (stmts_prime, fns) = loose_preprocess_functions(stmts,mname)
                new_func = (ast.Function(None, mname, args, [], 0, None, stmts_prime), fns)

                functionlist.append(new_func)

                retlist.append(ast.Assign([ast.AssName(name, 'OP_ASSIGN')],
                    FnName(mname)))
            else:
                print "I = ", i
                (new_i, functions) = loose_preprocess_functions(i)
                functionlist += functions
                retlist.append(new_i)

        return (ast.Stmt(retlist), functionlist)

    elif isinstance(pyast, (ast.Assign, ast.Add, ast.And, ast.Or)):
        rhs = pyast.getChildren()[1]
        lhs = pyast.getChildren()[0]
        (rhs_prime, rfns) = loose_preprocess_functions(rhs)
        (lhs_prime, lfns) = loose_preprocess_functions(lhs)
        if isinstance(pyast, ast.Assign):
            ret_prime = ast.Assign([lhs_prime], rhs_prime)
        else:
            ret_prime = pyast.__class__((lhs_prime, rhs_prime))
        return (ret_prime, rfns + lfns)
    
    elif isinstance(pyast, ast.Compare):
        rhs = pyast.getChildren()[2]
        op = pyast.getChildren()[1]
        lhs = pyast.getChildren()[0]
        (rhs_prime, rfns) = loose_preprocess_functions(rhs)
        (lhs_prime, lfns) = loose_preprocess_functions(lhs)
        ret_prime = ast.Compare(lhs_prime, [op,rhs_prime])
        return (ret_prime, rfns + lfns)
        

    elif isinstance(pyast, ast.Lambda):
        # and this is why this function is a bitch
        name = mangle(a_name, "%dlambda" % nonce)
        nonce += 1
        args = pyast.getChildren()[0]
        (stmt, fns) = loose_preprocess_functions(pyast.getChildren()[2], name)
        stmt_p = ast.Stmt([ast.Return(stmt)])
        fn = (ast.Function(None, name, args, [], 0, None, stmt_p), fns)

        return (FnName(name), [fn])

    elif isinstance(pyast, ast.CallFunc):
        lhs = pyast.getChildNodes()[0]
        args = pyast.getChildNodes()[1:]
        (lhs_prime, fns) = loose_preprocess_functions(lhs)
        args_p = map(loose_preprocess_functions, args)

        (args_prime, fns2) = zip(*args_p) if len(args_p) > 0 else ([],[])
        for i in fns2:
            fns += i
        return (ast.CallFunc(lhs_prime, args_prime), fns)

    elif isinstance(pyast, ast.Printnl):
        rhs = pyast.getChildNodes()[0] 
        (rhs_prime, fns) = loose_preprocess_functions(rhs)
        return (ast.Printnl([rhs_prime], None), fns)

    elif isinstance(pyast, (ast.Return, ast.Not, ast.UnarySub, ast.Discard)):
        rhs = pyast.getChildNodes()[0]
        (rhs_prime, fns) = loose_preprocess_functions(rhs)
        return (pyast.__class__(rhs_prime), fns)
        
    elif isinstance(pyast, (ast.Const, ast.Name, ast.AssName)):
        # these are the base cases
        return (pyast, [])
    
    elif isinstance(pyast, ast.If):
        (new_cond, funcs) = loose_preprocess_functions(pyast.getChildren()[0])
        (new_then, thenfuncs) = loose_preprocess_functions(pyast.getChildren()[1])
        if pyast.getChildren()[2] is not None:
            (new_else, elsefuncs) = loose_preprocess_functions(pyast.getChildren()[2])
        else:
            (new_else, elsefuncs) = (None, [])

        return (ast.If([(new_cond, new_then)], new_else), funcs + thenfuncs + elsefuncs)
    
    elif isinstance(pyast, ast.IfExp):
        (new_cond, funcs) = loose_preprocess_functions(pyast.getChildren()[0])
        (new_then, thenfuncs) = loose_preprocess_functions(pyast.getChildren()[1])
        (new_else, elsefuncs) = loose_preprocess_functions(pyast.getChildren()[2])

        return (ast.IfExp(new_cond, new_then, new_else), funcs + thenfuncs + elsefuncs)

    elif isinstance(pyast, ast.List):
        retlst = []
        fns = []
        for i in pyast.getChildren():
            (l, f) = loose_preprocess_functions(i)
            fns += f
            retlst.append(l)
        return (ast.List(retlst), fns)

    elif isinstance(pyast, ast.Subscript):
        (lhs, op, rhs) = pyast.getChildren()
        (lhsp, lhsf) = loose_preprocess_functions(lhs)
        (rhsp, rhsf) = loose_preprocess_functions(rhs)
        return (ast.Subscript(lhsp, op, [rhsp]), lhsf + rhsf)

    elif isinstance(pyast, ast.Dict):
        retlst = []
        fns = []
        for (k,v) in pyast.items:
            (kp, kf) = loose_preprocess_functions(k)
            (vp, vf) = loose_preprocess_functions(v)
            fns += kf + vf
            retlst.append((kp, vp))
        return (ast.Dict(retlst), fns)

        

    raise Exception("Unexpected " + str(pyast.__class__) + " in loose preprocess functions")
    

