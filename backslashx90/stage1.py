# this module is the spec of the intermediate
# language ast that implements the spec for
# the current project.

import compiler.ast as pyast
import viper.core as core

# Detect if the node is the base case
def is_base(pyst):
    return isinstance(pyst, pyast.Const) or \
           isinstance(pyst, pyast.Name)

#Convert Base Class to Value
def base_cov(pyst):
    if isinstance(pyst, pyast.Const):
        return core.Const(pyst.getChildren()[0] << 2);
    if isinstance(pyst, pyast.Name):
        return core.Name(pyst.getChildren()[0])

#Flattener Class
class Stage1:
    tempcount = 0
    def __init__(self, root=True):
        self.buffer = []
        if root:
            self.addAsm( core.Assign("True", core.Const(0b101)) )
            self.addAsm( core.Assign("False", core.Const(0b001)) )

#Create Temporary name
    def tmpvar(self, fmt="$%d$"):
        tmp = fmt % Stage1.tempcount
        Stage1.tempcount += 1
        return tmp

#Translate Base
    def trans(self, pyst, lhs, rhs):
        return \
            { pyast.Add: core.PyAdd,
              pyast.Div: core.Div,
              pyast.Mul: core.Mul
            }[pyst.__class__](lhs, rhs)

#Flatten an operation
    def loose_flatten_op(self, pyst):
        lhs, rhs = pyst.asList()
        lhs_, rhs_ = base_cov(lhs), base_cov(rhs)

        if is_base(lhs) and is_base(rhs):
            var = self.tmpvar()
            self.buffer += [core.Assign(var, self.trans(pyst, lhs_, rhs_))];
            return var

        else:
            if not is_base(lhs):
                var = self.loose_flatten(lhs)
                return self.loose_flatten(pyst.__class__((pyast.Name(var), rhs)))

            else:
                var = self.loose_flatten(rhs)
                return self.loose_flatten(pyst.__class__((lhs, pyast.Name(var))))

    def loose_flatten_func(self, pyst):
        lst = pyst.getChildNodes();
        lhs = lst[0]
        args = lst[1:]

        # flatten the arguments
        for i in range(len(args)):
            if not is_base(args[i]):
                var = self.loose_flatten(args[i])
                argsp = args[0:i] + (pyast.Name(var),) + args[i+1:]
                return self.loose_flatten(pyast.CallFunc(lhs, argsp, None, None))

        # args are flat for sure 
        var = self.tmpvar()
        self.buffer += [core.Assign(var, core.CallFunc(base_cov(lhs), args))]
        return var

    def addAsm(self, asm_node):
        self.buffer.append(asm_node)

    def loose_flatten_list(self, pyst):
        lst = pyst.getChildren()

        lst_name = self.tmpvar()
        self.buffer += [core.Assign(lst_name, core.CallFunc(core.Name("create_list"), [core.Const(len(lst)<<2)]))]

        data_ptr = self.tmpvar("$data_ptr_%d")
        self.buffer += [core.Assign(data_ptr, core.Deref(lst_name, 4))]

        self.buffer += [core.Assign( core.Deref(lst_name, 8), core.Const(len(lst))) ]

        i = 0
        for elem in lst:
            var = self.loose_flatten(elem);
            if var is None:
                self.buffer += [core.Assign( core.Deref(data_ptr,i), base_cov(elem) )]
            else:
                self.buffer += [core.Assign( core.Deref(data_ptr,i), core.Name(var) )]
            i += 4

        self.buffer += [core.Assign(lst_name, core.Add(core.Name(lst_name), core.Const(3)))]

        return lst_name

    def try_var(self, varname, orig):
        if varname is None:
            return base_cov(orig)
        else:
            return core.Name(varname)
    def flatten_to_var(self, orig):
        tmp = self.loose_flatten(orig)
        ret = self.try_var(tmp, orig)
        return ret
        
    def loose_flatten_if(self, pyst):
        cond = self.flatten_to_var( pyst.getChildren()[0] )

        then_nodes = pyst.getChildren()[1]
        if pyst.getChildren()[2] is None:
            else_nodes = []
        else:
            else_nodes = flatten(pyst.getChildren()[2])

        self.addAsm(core.If(cond, flatten(then_nodes), else_nodes))
        return None
        
    def loose_flatten_ifexpr(self, pyst):
        cond = pyst.getChildren()[0]
        var = self.tmpvar()

        new_if = pyast.If( [(cond, 
            pyast.Stmt([pyast.Assign([pyast.AssName(var, 'OP_ASSIGN')], pyst.getChildren()[1])]))],
            pyast.Stmt([pyast.Assign([pyast.AssName(var, 'OP_ASSIGN')], pyst.getChildren()[2])]), None )

        self.loose_flatten_if(new_if)
        return var


    def loose_flatten_dict(self, pyst):
        dct_children = pyst.getChildren()
        dct_name = self.tmpvar()

        self.addAsm( core.Assign(dct_name, core.CallFunc(core.Name("create_dict"), [])) )
        self.addAsm( core.Assign(dct_name, core.Add(core.Name(dct_name), core.Const(3))) )

        i = len(dct_children)-2
        while i >= 0:
            key_var = self.loose_flatten(dct_children[i])
            val_var = self.loose_flatten(dct_children[i+1])

            key_arg = core.Name(key_var) if not key_var is None else base_cov(dct_children[i])
            val_arg = core.Name(val_var) if not val_var is None else base_cov(dct_children[i+1])

            self.addAsm( 
                core.Assign(self.tmpvar(), core.CallFunc(core.Name("set_subscript"), [core.Name(dct_name), key_arg, val_arg])) )
            i -= 2

        return dct_name

    def loose_flatten_bool_and(self, pyst):
        var = self.unbasecov(self.flatten_to_var(pyst.getChildren()[0]))
        if_stmt = pyast.IfExp(var, pyst.getChildren()[1], var)
        return self.loose_flatten_ifexpr(if_stmt)

    def unbasecov(self, viperast):
        if isinstance(viperast, core.Const):
            return pyast.Const(viperast.raw >> 2)
        elif isinstance(viperast, core.Name):
            return pyast.Name(viperast.name)

    def loose_flatten_bool_or(self, pyst):
        var = self.unbasecov(self.flatten_to_var(pyst.getChildren()[0]))
        if_stmt = pyast.IfExp(var, var, pyst.getChildren()[1])
        return self.loose_flatten_ifexpr(if_stmt)

    def loose_flatten_subscript(self, pyst):
        children = pyst.getChildren()
        lhs, rhs = (children[0], children[2])
        lhs_, rhs_ = base_cov(lhs), base_cov(rhs)

        print "PYST",pyst,"|",children
        print "RHS_CLASS",rhs.__class__

        if is_base(lhs) and is_base(rhs):
            var = self.tmpvar()
            self.buffer += [core.Assign(var, core.Subscript(lhs_, rhs_))];
            return var

        else:
            if not is_base(lhs):
                var = self.loose_flatten(lhs)
                tmp = pyast.Subscript(pyast.Name(var), 'OP_APPLY', [rhs])
                return self.loose_flatten(tmp)

            else:
                var = self.loose_flatten(rhs)
                tmp = pyast.Subscript(lhs, 'OP_APPLY', [pyast.Name(var)])
                return self.loose_flatten(tmp)
        
    # returns variable assigned to
    def loose_flatten(self, pyst):
        if is_base(pyst):
            # already flat
            return None

        if isinstance(pyst, pyast.Add) or \
           isinstance(pyst, pyast.Mul) or \
           isinstance(pyst, pyast.Div):
           # if arithmetic

            return self.loose_flatten_op(pyst)

        if isinstance(pyst, pyast.CallFunc):
            return self.loose_flatten_func(pyst)

        if isinstance(pyst, pyast.List):
            return self.loose_flatten_list(pyst)

        if isinstance(pyst, pyast.Dict):
            return self.loose_flatten_dict(pyst)

        if isinstance(pyst, pyast.If):
            return self.loose_flatten_if(pyst)

        if isinstance(pyst, pyast.And):
            return self.loose_flatten_bool_and(pyst)

        if isinstance(pyst, pyast.Or):
            return self.loose_flatten_bool_or(pyst)

        if isinstance(pyst, pyast.Subscript):
            return self.loose_flatten_subscript(pyst)

        if isinstance(pyst, pyast.Compare):
            return self.loose_flatten_compare(pyst)

        if isinstance(pyst, pyast.Not):
            rhs = pyst.getChildren()[0]
            if is_base( rhs ):
                var = self.tmpvar()
                self.buffer += [core.Assign(var, core.Not(base_cov(rhs)))];
                return var
            else:
                var = self.loose_flatten(rhs);
                return self.loose_flatten(pyast.Not(pyast.Name(var)));

            return

        if isinstance(pyst, pyast.UnarySub):
            rhs = pyst.getChildren()[0]
            if is_base( rhs ):
                var = self.tmpvar()
                self.buffer += [core.Assign(var, core.Neg(base_cov(rhs)))];
                return var
            else:
                var = self.loose_flatten(rhs);
                return self.loose_flatten(pyast.UnarySub(pyast.Name(var)));

            return

        if isinstance(pyst, pyast.IfExp):
            return self.loose_flatten_ifexpr(pyst)

        else:
            raise Exception('Unexpected in loose flatten ' + pyst.__class__.__name__)

    def loose_flatten_compare(self, pyst):
        #Restruc
        array = pyst.getChildren()
        print "ARRAY ", array

        if len(array) <= 3:
            # this is the base case
            lhs = array[0]
            op = array[1]
            rhs = array[2]

            lhs_flat = self.flatten_to_var(lhs)
            rhs_flat = self.flatten_to_var(rhs)

            var = self.tmpvar()
            if op == "==":
                self.buffer += [core.Assign(var, core.Equals(lhs_flat, rhs_flat))]
            elif op == "is":
                self.buffer += [core.Assign(var, core.Is(lhs_flat, rhs_flat))]
            return var



        current_compare = pyast.Compare( array[0], [array[1], array[2]] )
        compare1 = pyast.Compare(array[2], [array[3], array[4]])

        current_and = pyast.And( (current_compare, compare1) )

        i = 5
        while i < len(array):
            current_compare = pyast.Compare( array[i-1], [array[i], array[i+1]] )
            current_and = pyast.And( (current_and, current_compare) )
            i += 2
        
        print "CURRENT_CMP: ", current_compare
        print "CURRENT_AND: ", current_and
        #Flatten New Tree
        return self.loose_flatten( current_and )

#Flatten Assignment
    def flatten_assign(self, pyst):
        if isinstance(pyst, pyast.Assign):
            if isinstance(pyst.getChildren()[0], pyast.Subscript):
                subscr = pyst.getChildren()[0]
                children = subscr.getChildren()
                lhs, rhs = (children[0], children[2])

                var = self.flatten_to_var(lhs)
                rhs_flat = self.flatten_to_var(rhs)
                to_assign = self.flatten_to_var(pyst.getChildren()[1])

                retvar = self.tmpvar()

                callfunc = core.CallFunc(core.Name("set_subscript"), [var, rhs_flat, to_assign])
                self.buffer += [core.Assign(retvar, callfunc)]
                return retvar

            else:
                # if instance of assign, flatten the rhs
                var = self.loose_flatten(pyst.getChildren()[1])
    
                # var = None if no temp var needed, or name of temp var
                if var is None:
                    # already flat, convert from python ast -> stage1 ast
                    rhs = base_cov(pyst.getChildren()[1])
                else:
                    # rhs = name of var e.g. $1$
                    rhs = core.Name(var)
    
                # append to the buffer an assignment
                self.buffer += [core.Assign(pyst.getChildren()[0].getChildren()[0], rhs)]
        else:
            raise Exception("Expected an Assign instance")

#Flatten Print
    def flatten_print(self, pyst):
        if isinstance(pyst, pyast.Printnl):
            var = self.loose_flatten(pyst.getChildren()[0]);

            if var is None:
                rhs = base_cov(pyst.getChildren()[0])
            else:
                rhs = core.Name(var);

            self.buffer += [core.Print(rhs)]

        else:
            raise Exception("Expected an Printnl instance")

#Flatten the tree
    def flatten(self, pyst):
        if isinstance(pyst, pyast.Assign):
            self.flatten_assign(pyst)

        elif isinstance(pyst, pyast.Module):
            # ignore module
            self.flatten(pyst.getChildren()[1])

        elif isinstance(pyst, pyast.Stmt):
            # go through all children and flatten
            for i in pyst.getChildren():
                self.flatten(i)

        elif isinstance(pyst, pyast.CallFunc):
            self.loose_flatten(pyst);

        elif isinstance(pyst, pyast.Discard):
            self.flatten(pyst.getChildren()[0])

        elif isinstance(pyst, pyast.Add):
            self.loose_flatten(pyst)

        elif isinstance(pyst, pyast.If):
            self.loose_flatten(pyst)

        elif isinstance(pyst, pyast.UnarySub):
            self.loose_flatten(pyst);

        elif isinstance(pyst, pyast.Printnl):
            self.flatten_print(pyst);

        elif isinstance(pyst, pyast.List):
            self.loose_flatten(pyst)

        elif isinstance(pyst, pyast.Compare):
            self.loose_flatten(pyst)

        elif is_base(pyst):
            return base_cov(pyst)

        else:
            raise Exception("Unexpected " + pyst.__class__.__name__)

        return self.buffer

# simply call flatten on a stage1
def flatten(ast, root=False):
    sg1 = Stage1(root)
    return sg1.flatten(ast)

#print the flatten ast
def print_core_ast( core ): # core : [AST]
    return "\n".join([i._to_str() for i in core])
