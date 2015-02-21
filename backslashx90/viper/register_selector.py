#This class Allocates Registers

from AsmTree import *
from viper.AsmTypes import SPILL, CALLER_SAVED, RAW, CONSTANT, AsmVar

REG_MAP = { 0: "%eax", 1: "%ebx", 2: "%ecx", 3: "%edx",
            4: "%edi", 5: "%esi" }
CALLER_REGISTERS = set( [0, 2, 3] )
NREG = 6

# Allocate Registers
# return (tree, nstackvars)
def allocate_registers( asm_tree ):
    #Build the interference model
    alloc = Allocation()

    sets_asm = list(alloc.build_interference_model( asm_tree[:] ))
    sets_asm.reverse()

    print "------------- Liveness"
    for x in sets_asm:
        print "%-40s %s" % x

    print "-------------"

    (_, sets) = zip( *sets_asm ) if len(sets_asm) > 0 else ([],[])
   
    #Build the Color Graph
    graph = alloc.build_graph( sets_asm );

    print "\n-----------INTERFERENCE--------------"
    for x in graph:
        print "\n", x, "-> ", 
        for y in graph[x]:
            print y, " ",
    print "--------------"

    (colors, n_stack_vars) = alloc.color_graph( graph )

    print "\n---------- Edge Detection"
    alloc.print_graph(colors)
    print "------------\n"


    print "------------ ASM BEFORE SPILLING"
    for x in asm_tree:
        print x

    print "--------------\n"
    # returns None if pass
    # If there was a spill then generate spill code
    new_asm = alloc.pass_spill( asm_tree, colors )

    print "----------- Asm After Spilling"
    if new_asm:
        print "Spilled our code"
    else:
        print "We did not spill"
    print "------------\n"
    if new_asm:
        return allocate_registers( new_asm )
    else:
        asm_tree = alloc.flatten_ifs(asm_tree)
        print "---- Before Simple Sub ---"
        for x in asm_tree:
            print x
        print"----\n"

        alloc.simple_sub(asm_tree, colors)
        print "-----After Simple Sub---"
        for y in asm_tree:
            print y
        print "--------\n"

        print "------COLORS AFTER SIMPLE SUB---"
        for x in colors:
            print x, " = ", colors[x]
    
        print "--------\n\n"
        asm_tree = list(alloc.remove_trivial(asm_tree))


    return [Subl(AsmVar("%s" % ((n_stack_vars+2)*4), CONSTANT), AsmVar("%esp", RAW))] + asm_tree

#The Allocation class provides all register allocation functionality
class Allocation:
    def __init__(self):
        self.current_temp = 0

    def flatten_ifs(self, asm_tree):
        buf = []
        for instr in asm_tree:
            if isinstance(instr, If):
                for i in self.flatten_ifs(instr.else_stmts):
                    buf.append(i)
                for i in self.flatten_ifs(instr.then_stmts):
                    buf.append(i)
            else:
                buf.append(instr)
        return buf
        

    #Returns the mapping for variables to colors
    def get_mapping( self, color ):
        if color < NREG:
            return REG_MAP[color]
        return "-%d(%%ebp)" % ((color - NREG + 1)*4)
    
    #Turns the Var into a asm
    def to_asm( self, var, colors ):
        print "VAR " + str(var)
        if var.isConstant(): # constant
            return var
        if var.isRaw(): # constant
            return var
        else:
            return AsmVar(self.get_mapping( colors[var] ) + "", var.mask, var.dref_off)

    #changes all variable names
    def simple_sub( self, asm_tree, colors ):
        for instr in asm_tree:
            instr.map_vars(lambda s: self.to_asm(s, colors))

    #Remove trivial instructions
    def remove_trivial( self, asm_tree ):
        for instr in asm_tree:
            if not (isinstance(instr, Movl) and
                    instr.lhs.getName() == instr.rhs.getName()):
                    yield instr
    
    #Checks if the color is a register
    def is_register( self, color ):
        return color < NREG

    def is_memory(self, name, colors):
        if name.isMemory():
            return True
        if not self.is_var(name):
            return False
        slot = colors[name]
        return not self.is_register(slot)
    
    #Runs the spill code generator
    def pass_spill( self, asm_tree, colors ):
        did_spill = False
   
        # TODO spill broken for dereferences
        ret_list = []
        for instr in asm_tree:
            inst_class = instr.__class__
            if isinstance(instr, Movl) or isinstance(instr, Addl) \
                or isinstance(instr, Andl):

                s, d = instr.lhs, instr.rhs;
                if self.is_memory(s,colors) and self.is_memory(d,colors):
                    t_slot = AsmVar("%d" % self.current_temp, SPILL )
                    self.current_temp += 1
                    ret_list.append( Movl(s, t_slot) )
                    ret_list.append( inst_class(t_slot, d) )
                    did_spill = True
                else:
                    ret_list.append( instr )

            elif isinstance( instr, If ):
                then_asm = self.pass_spill(instr.then_stmts, colors)
                else_asm = self.pass_spill(instr.else_stmts, colors)

                if then_asm or else_asm:
                    did_spill = True

                new_instr = If(instr.cond, [], [])
                new_instr.then_stmts = then_asm or instr.then_stmts
                new_instr.else_stmts = else_asm or instr.else_stmts

                ret_list.append(new_instr)
    
            else:
                ret_list.append(instr)
    
        if did_spill:
            return ret_list
        else:
            return None
                
    #Print the color graph 
    def print_graph( self, graph_map):
        for key, vals in graph_map.items():
            print ("%s -> %s" % (key, vals))
    
    #Add an edge to the mapping
    def add_interfere( self, mapping, t, v ):
        if t not in mapping:
            mapping[t] = set()
        if v not in mapping:
            mapping[v] = set()
        mapping[t].add(v)
        mapping[v].add(t)
    
    
    #Builds the interference Graph
    # returns map (string -> set(string))
    def build_graph( self, sets ):
        ret_map = dict()
        for instr, l_after in sets:
            if isinstance( instr, Movl ):
    
                t = instr.rhs
                s = instr.lhs

                if self.is_var(t):
        
                    if not t in ret_map:
                        ret_map[t] = set()
                    for v in l_after:
                        if v != t: # and v != s:
                            self.add_interfere( ret_map, v, t )
    
            if isinstance(instr, Addl) or isinstance(instr, Andl):
                
                t = instr.rhs
                s = instr.lhs
    
                if self.is_var(t):
                    if not t in ret_map:
                        ret_map[t] = set()
                    for v in l_after:
                        if v != t:
                            self.add_interfere( ret_map, v, t )
    
            if isinstance( instr, Neg ):
                t = instr.val
                if not t in ret_map:
                    ret_map[t] = set()
                for v in l_after:
                    if v != t:
                        self.add_interfere( ret_map, v, t )
    
            if isinstance( instr, Push ):
                t = instr.val

                if self.is_var(t):
                    if not t in ret_map:
                        ret_map[t] = set()
                    for v in l_after:
                        if v != t:
                            self.add_interfere( ret_map, v, t )
    
        return ret_map
    
    
    #color the Interference Graph
    #(map(string -> int), nvars)
    def color_graph( self, mapping):
        ret_map = dict()
    
        maxret = 0
    
        for node in mapping:
            # priority given to nodes with a ^ (must be a register)
            if node.cantSpill():
                neighbors = mapping[node] # set
                possible = set(range(len(neighbors) + 1)) # possible registers
        
                for neighbor in neighbors:
                    if neighbor in ret_map and ret_map[neighbor] in possible:
                        possible.remove( ret_map[neighbor] )
        
                ret_map[node] = min(possible)
                maxret = max( maxret, ret_map[node] )
    
        for node in mapping:
            # these nodes cannot be given to a caller register
            if node.isCallerSaved():
                neighbors = mapping[node] # set
                possible = set(range(len(neighbors) + 4)) - CALLER_REGISTERS # possible registers
        
                for neighbor in neighbors:
                    if neighbor in ret_map and ret_map[neighbor] in possible:
                        possible.remove( ret_map[neighbor] )
        
                ret_map[node] = min(possible)
                maxret = max( maxret, ret_map[node] )
    
        for node in mapping:
            if not node.cantSpill() and not node.isCallerSaved():
                neighbors = mapping[node] # set
                possible = set(range(len(neighbors) + 1)) # possible registers
        
                for neighbor in neighbors:
                    if neighbor in ret_map and ret_map[neighbor] in possible:
                        possible.remove( ret_map[neighbor] )
        
                ret_map[node] = min(possible)
                maxret = max( maxret, ret_map[node] )
    
        maxret -= NREG
        maxret = maxret if maxret > 0 else 0
        return (ret_map, maxret)
    
    #Checks if it is a variable that can cause interference
    def is_var( self, name):
        return not name.isRaw() and not name.isConstant()

    #Create a list of live variables after each instuction
    def build_interference_model( self, asm_tree, current_set = set() ):
        reverse_asm_tree = asm_tree[:]
        reverse_asm_tree.reverse()
    
        # yield (None, set())
        for instr in reverse_asm_tree:
            if isinstance( instr, Movl ):
                src = instr.lhs
                dest = instr.rhs
    
                if dest in current_set and dest:
                    current_set.remove( dest )

                if dest.is_deref():
                    current_set.add( dest.to_basic() )
    
                if self.is_var(src):
                    current_set.add( src.to_basic() )
        
            elif isinstance( instr, Addl ) or isinstance(instr, Andl):
                rhs = instr.rhs
                lhs = instr.lhs
    
                if self.is_var(rhs):
                    current_set.add( rhs )
                if self.is_var(lhs):
                    current_set.add( lhs )
    
            elif isinstance( instr, Neg ):
                rhs = instr.val
                if self.is_var(rhs):
                    current_set.add( rhs )
    
            elif isinstance( instr, Push ):
                rhs = instr.val
                if self.is_var(rhs):
                    current_set.add( rhs )
    
            elif isinstance( instr, Call):
                name = instr.name

            elif isinstance( instr, If ):
                print "HELLO"
                then_stmts = instr.then_stmts
                else_stmts = instr.else_stmts
                lst1 = list(self.build_interference_model(then_stmts, current_set.copy()))
                lst2 = list(self.build_interference_model(else_stmts, current_set.copy()))

                set1 = lst1[-1][1]
                set2 = lst2[-1][1]
                current_set |= set1 | set2

                for i in lst1:
                    yield i
                for i in lst2:
                    yield i
                
                
    
            if not isinstance( instr, If ):
                yield (instr, current_set.copy())