#This class Allocates Registers

from AsmTree import Movl, Addl, Neg, Push, Pop, Call, Subl
from viper.AsmTypes import SPILL, CALLER_SAVED, RAW, CONSTANT, AsmVar

REG_MAP = { 0: "%eax", 1: "%ebx", 2: "%ecx", 3: "%edx",
            4: "%edi", 5: "%esi" }
CALLER_REGISTERS = set( [0, 2, 3] )
NREG = 6

# return (tree, nstackvars)
def allocate_registers( asm_tree ):
    #Build the interference model
    alloc = Allocation()

    sets = list(alloc.build_interference_model( asm_tree ))
    sets.reverse()
    sets = zip(asm_tree, sets[1:])

    print "------------- Liveness"
    for x in sets:
        print x

    print "-------------"
   
    #Build the Color Graph
    graph = alloc.build_graph( sets );

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
        print "---- Before Simple Sub ---"
        for x in asm_tree:
            print x
        print"----\n"

    #NOTE: BUG IS RIGHT HERE
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

class Allocation:
    def __init__(self):
        self.current_temp = 0

    def get_mapping( self, color ):
        if color < NREG:
            return REG_MAP[color]
        return "-%d(%%ebp)" % ((color - NREG + 1)*4)
    
    def to_asm( self, var, colors ):
        if var.isConstant(): # constant
            return var
        if var.isRaw(): # constant
            return var
        else:
            return AsmVar(self.get_mapping( colors[var] ) + "", var.mask)
    
    def simple_sub( self, asm_tree, colors ):
        for instr in asm_tree:
            instr.map_vars(lambda s: self.to_asm(s, colors))
    
    def remove_trivial( self, asm_tree ):
        for instr in asm_tree:
            if not (isinstance(instr, Movl) and
                    instr.src.getName() == instr.dest.getName()):
                    yield instr
    
    
    def is_register( self, color ):
        return color < NREG
    
    def pass_spill( self, asm_tree, colors ):
        did_spill = False
   
        print "=======SPILLED======" 
        ret_list = []
        for instr in asm_tree:
            if isinstance( instr, Movl ):
                print "===MOVL==="
                s, d = instr.src, instr.dest;
                if self.is_var(s) and self.is_var(d):
                    print "===isvars===", "s = ", s , " d = ", d
                    s_slot, d_slot = colors[s], colors[d]
                    # check for a spill
                    if not (self.is_register(s_slot) or self.is_register(d_slot)): 
                        print "==IN REGES=="
                        t_slot = AsmVar("%d" % self.current_temp, SPILL )
                        self.current_temp += 1
                        ret_list.append( Movl(s, t_slot) )
                        ret_list.append( Movl(t_slot, d) )
                        did_spill = True
                    else:
                        ret_list.append( instr )
                else:
                    ret_list.append( instr )
    
            elif isinstance( instr, Addl ):
                s, d = instr.lhs, instr.rhs;
                if self.is_var(s) and self.is_var(d):
                    s_slot, d_slot = colors[s], colors[d]
                    # check for a spill
                    if not (self.is_register(s_slot) or self.is_register(d_slot)): 
                        t_slot = AsmVar("%d" % self.current_temp, SPILL)
                        self.current_temp += 1
                        ret_list.append( Movl(s, t_slot) )
                        ret_list.append( Addl(t_slot, d) )
                        did_spill = True
                    else:
                        ret_list.append( instr )
                else:
                    ret_list.append( instr )
    
            else:
                ret_list.append(instr)
    
        if did_spill:
            return ret_list
        else:
            return None
                
    
    def print_graph( self, graph_map):
        for key, vals in graph_map.items():
            print ("%s -> %s" % (key, vals))
    
    def add_interfere( self, mapping, t, v ):
        if t not in mapping:
            mapping[t] = set()
        if v not in mapping:
            mapping[v] = set()
        mapping[t].add(v)
        mapping[v].add(t)
    
    
    #interference graph
    # returns map (string -> set(string))
    def build_graph( self, sets ):
        ret_map = dict()
        for instr, l_after in sets:
            if isinstance( instr, Movl ):
    
                t = instr.dest
                s = instr.src
    
                if not t in ret_map:
                    ret_map[t] = set()
                for v in l_after:
                    if v != t: # and v != s:
                        self.add_interfere( ret_map, v, t )
    
            if isinstance( instr, Addl ):
                
                t = instr.rhs
                s = instr.lhs
    
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
                if not t in ret_map:
                    ret_map[t] = set()
                for v in l_after:
                    if v != t:
                        self.add_interfere( ret_map, v, t )
    
        return ret_map
    
    
    #color the graph
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
            if node.isNormal():
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
    
    def is_var( self, name):
        return not name.isRaw() and not name.isConstant()
    
    #liveness analysis
    def build_interference_model( self, asm_tree ):
        reverse_asm_tree = asm_tree[:]
        reverse_asm_tree.reverse()
    
        yield set()
        current_set = set()
        for instr in reverse_asm_tree:
            if isinstance( instr, Movl ):
                src = instr.src
                dest = instr.dest
    
                if dest in current_set:
                    current_set.remove( dest )
    
                if self.is_var(src):
                    current_set.add( src )
        
            elif isinstance( instr, Addl ):
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
                
    
            yield current_set.copy()
