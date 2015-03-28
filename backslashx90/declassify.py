import compiler.ast as ast

def declassify(ast):
    declass = declassifier()
    return declass.declassify(ast)


class declassifier:
    def __init__(self):
        pass
    def declassify(self,a_ast):
        nodes = a_ast.getChildren()
        print "NODES", str(nodes)
        retnodes = []
        for stmt in nodes:
            print "STMT",stmt
            if isinstance(stmt, ast.Class):
                print "The statement is a CLASS MOFO!!!"

                clazz = stmt
                (class_stmts,) = clazz.getChildNodes()
                class_name = clazz.getChildren()[0]
                retnodes.append(ast.Assign([ast.AssName(class_name, 'OP_ASSIGN')], MkClass()));
                for i in class_stmts:
                    if isinstance(i, ast.Assign):
                        (assname, rhs) = i.getChildNodes()
                        name = assname.getChildren()[0]
                        retnodes.append(SetAttr(ast.Name(class_name), name, rhs))
                    else:
                        retnodes.append(i)
            else:
                retnodes.append(stmt)
        return ast.Stmt(retnodes);

class SetAttr:
    def __init__(self, lhs, attr, rhs):
        # attr :: String
        self.lhs = lhs
        self.attr = attr 
        self.rhs = rhs

    def __str__(self):
        return "SetAttr(%s, %s)" % (self.lhs, self.attr)

class GetAttr:
    def __init__(self, lhs, attr):
        self.lhs = lhs
        self.attr = attr

    def __str__(self):
        return "GetAttr(%s, %s)" % (self.lhs, self.attr)
        
class MkClass:
    def __init__(self):
        pass

    def __str__(self):  
        return "MkClass()"
