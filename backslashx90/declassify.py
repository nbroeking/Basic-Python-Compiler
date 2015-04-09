import compiler.ast as ast
import function_comb as fn

def declassify(ast):
    declass = declassifier()
    return declass.declassify(ast)


class declassifier:
    def __init__(self):
        pass
    def declassify_p(self,a_ast,current_class):
        nodes = a_ast.getChildren()
        print "NODES", str(nodes)
        self.mark_nodes(current_class, a_ast)
        retnodes = []
        for stmt in nodes:
            print "STMT",stmt
            if isinstance(stmt, ast.Class):
                print "The statement is a CLASS MOFO!!!"

                clazz = stmt
                class_stmts = clazz.getChildNodes()[-1]

                class_name = clazz.getChildren()[0]

                #
                pass_down = ast.Name(class_name) if current_class == None else GetAttr(current_class, class_name)
                print "PASS_DOWN: ", pass_down
                #
                class_stmts = self.declassify_p(class_stmts, pass_down)


                print "RIGHT HERE TAG + SHIT " + str(clazz.getChildNodes())
                bases = clazz.getChildNodes()[0:-1]

                retnodes.append(ast.Assign([ast.AssName("$class_bases_", 'OP_ASSIGN')], ast.List(bases)))
                retnodes.append(ast.Assign([ast.AssName(class_name, 'OP_ASSIGN')], MkClass(ast.Name("$class_bases_"))));
                retnodes.append(SetAttr(pass_down, "__init__", fn.FnName("_default_init_fn_")))

                # replace all ast.Names with IfExpr(HasAttr(clazz, Name), GetAttr(clazz, Name), Name)
                
                def transform_assign(stmts): # -> [stmts]
                    retlist = []

                    for i in stmts:
                        if isinstance(i, ast.Assign) and i.getChildren()[0] != "$class_bases_":
                            """ Assign to the class name instead """
                            (assname, rhs) = i.getChildNodes()
                            name = assname.getChildren()[0]
                            retlist.append(SetAttr(pass_down, name, rhs))

                        elif isinstance(i, ast.If):
                            (cond, thens, elses) = i.getChildren()
                            thens_p = transform_assign(thens)
                            elses_p = transform_assign(elses) if elses else None
                            retnodes.append(ast.If([(cond,ast.Stmt(thens_p))], ast.Stmt(elses_p)))

                        elif isinstance(i, ast.While):
                            print "THIS IS A WHILE STATEMENT SON"
                            (cond, thens, _) = i.getChildren()
                            stmts_p = transform_assign(thens)
                            retnodes.append(ast.While(cond, ast.Stmt(stmts_p), None))
                
                        else:
                            retlist.append(i)

                    return retlist

                for i in transform_assign(class_stmts):
                    retnodes.append(i)

            elif isinstance(stmt, ast.If):
                (cond, thens, elses) = stmt.getChildren()
                thens_p = self.declassify_p(thens, current_class)
                elses_p = self.declassify_p(elses, current_class) if elses else None
                retnodes.append(ast.If([(cond,ast.Stmt(thens_p))], ast.Stmt(elses_p)))

            elif isinstance(stmt, ast.While):
                print "THIS IS A WHILE STATEMENT SON"
                (cond, stmts, _) = stmt.getChildren()
                stmts_p = self.declassify_p(stmts, current_class)
                retnodes.append(ast.While(cond, ast.Stmt(stmts_p), None))
                
            else:
                retnodes.append(stmt)
        return retnodes;
    
    def mark_nodes(self, clazz_name, a_ast):
        for i in a_ast.getChildNodes():
            if isinstance(i, ast.Name):
                i.clazz_name = clazz_name # mark a name as being a part of a class

    def declassify(self, a_ast):
        return ast.Stmt(self.declassify_p(a_ast, None))

class UnboundMethod:
    def __init__(self, name):
        self.name = name

    def getChildNodes(self):
        return []

    def getChildren(self):
        return []

    def _to_str(self):
        return "UnboundMethod(%s)" % self.name

    def __str__(self):
        return self._to_str()

    def __repr__(self):
        return self._to_str()

class SetAttr:
    def __init__(self, lhs, attr, rhs):
        # attr :: String
        self.lhs = lhs
        self.attr = attr 
        self.rhs = rhs

    def getChildNodes(self):
        return [self.lhs, self.rhs]

    def _to_str(self):
        return self.__str__()

    def __repr__(self):
        return self._to_str()

    def __str__(self):
        return "SetAttr(%s, %s, %s)" % (self.lhs, self.attr, self.rhs)


class GetAttr:
    def __init__(self, lhs, attr):
        self.lhs = lhs
        self.attr = attr

    def getChildNodes(self):
        return [self.lhs]

    def getChildren(self):
        return self.getChildNodes()

    def _to_str(self):
        return self.__str__()

    def __repr__(self):
        return self._to_str()

    def __str__(self):
        return "GetAttr(%s, %s)" % (self.lhs, self.attr)

class HasAttr:
    pass
        
class MkClass:
    def __init__(self, bases):
        self.bases = bases
        pass

    def getChildNodes(self):
        return self.bases

    def getChildren(self):
        return self.bases

    def __str__(self):  
        return "MkClass(%s)" % str(self.bases)
