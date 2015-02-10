from AsmTree import Movl, Addl, Neg, Push, Pop, Call, Subl

REG_MAP = { 0: "%eax", 1: "%ebx", 2: "%ecx", 3: "%edx",
            4: "%edi", 5: "%esi" }
NREG = 6

def allocate_registers( asm_tree ):
    # edge_list : [[string]]
    sets = list(build_interference_model( asm_tree ))
    sets.reverse()
    sets = zip(asm_tree, sets[1:])

    for (i,(_,j)) in zip(asm_tree, sets):
        print ("%-20s | %s" % (i,j))
    print "----------------"

    graph = build_graph(sets)
    print_graph(graph)
    print "----------------"

    colors = color_graph( graph )
    print_graph(colors)

    # returns None if pass
    new_asm = pass_spill( asm_tree, colors )
    if new_asm:
        print "==== SPILL ===="
        return allocate_registers( new_asm )
    else:
        print "---------------"
        for i in asm_tree:
            print i
        simple_sub(asm_tree, colors)
        print "---------------"
        for i in asm_tree:
            print i
        asm_tree = list(remove_trivial(asm_tree))
        print "---------------"
        for i in asm_tree:
            print i


    return asm_tree

def get_mapping( color ):
    if color < NREG:
        return REG_MAP[color]
    return "-%d(%%ebp)" % ((color - NREG + 1)*4)

def to_asm( string, colors ):
    if string[0] == '&': # constant
        return '$' + string[1:]
    if string[0] == '%': # constant
        return string[1:]
    else:
        return get_mapping( colors[string] )

def simple_sub( asm_tree, colors ):
    for instr in asm_tree:
        instr.map_vars(lambda s: to_asm(s, colors))

def remove_trivial( asm_tree ):
    for instr in asm_tree:
        if not (isinstance(instr, Movl) and
                instr.src == instr.dest):
                yield instr


def is_register( color ):
    return color < NREG

def pass_spill( asm_tree, colors ):
    current_temp = 0 # temp counter
    did_spill = False

    ret_list = []
    for instr in asm_tree:
        if isinstance( instr, Movl ):
            s, d = instr.src, instr.dest;
            if is_var(s) and is_var(d):
                s_slot, d_slot = colors[s], colors[d]
                # check for a spill
                if not (is_register(s_slot) or is_register(d_slot)): 
                    t_slot = "^%d" % current_temp
                    current_temp += 1
                    ret_list.append( Movl(s_slot, t_slot) )
                    ret_list.append( Movl(t_slot, d_slot) )
                    did_spill = True
                else:
                    ret_list.append( instr )
            else:
                ret_list.append( instr )

        if isinstance( instr, Addl ):
            s, d = instr.lhs, instr.rhs;
            if is_var(s) and is_var(d):
                s_slot, d_slot = colors[s], colors[d]
                # check for a spill
                if not (is_register(s_slot) or is_register(d_slot)): 
                    t_slot = "^%d" % current_temp
                    current_temp += 1
                    ret_list.append( Movl(s_slot, t_slot) )
                    ret_list.append( Addl(t_slot, d_slot) )
                    did_spill = True
                else:
                    ret_list.append( instr )
            else:
                ret_list.append( instr )

    if did_spill:
        return ret_list
    else:
        return None
            

def print_graph(graph_map):
    for key, vals in graph_map.items():
        print ("%s -> %s" % (key, vals))

def add_interfere( mapping, t, v ):
    if t not in mapping:
        mapping[t] = set()
    if v not in mapping:
        mapping[v] = set()
    mapping[t].add(v)
    mapping[v].add(t)


#interference graph
# returns map (string -> set(string))
def build_graph( sets ):
    ret_map = dict()
    for instr, l_after in sets:
        if isinstance( instr, Movl ):

            t = instr.dest
            s = instr.src

            ret_map[t] = set()
            for v in l_after:
                if v != t: # and v != s:
                    add_interfere( ret_map, v, t )

        if isinstance( instr, Addl ):
            
            t = instr.rhs
            s = instr.lhs

            ret_map[t] = set()
            for v in l_after:
                if v != t:
                    add_interfere( ret_map, v, t )
    return ret_map


#color the graph
#map(string -> int)
def color_graph( mapping):
    ret_map = dict()

    for node in mapping:
        # priority given to nodes with a ^ (must be a register)
        if node.startswith("^"):
            neighbors = mapping[node] # set
            possible = set(range(len(neighbors) + 1)) # possible registers
    
            for neighbor in neighbors:
                if neighbor in ret_map and ret_map[neighbor] in possible:
                    possible.remove( ret_map[neighbor] )
    
            ret_map[node] = min(possible)

    for node in mapping:
        if not node.startswith("^"):
            neighbors = mapping[node] # set
            possible = set(range(len(neighbors) + 1)) # possible registers
    
            for neighbor in neighbors:
                if neighbor in ret_map and ret_map[neighbor] in possible:
                    possible.remove( ret_map[neighbor] )
    
            ret_map[node] = min(possible)

    return ret_map

def is_var(name):
    return len(name) > 0 and name[0] != '&' and name[0] != '%'

#liveness analysis
def build_interference_model( asm_tree ):
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

            if is_var(src):
                current_set.add( src )
    
        elif isinstance( instr, Addl ):
            rhs = instr.rhs
            lhs = instr.lhs

            if is_var(rhs):
                current_set.add( rhs )
            if is_var(lhs):
                current_set.add( lhs )

        elif isinstance( instr, Neg ):
            rhs = instr.val
            if is_var(rhs):
                current_set.add( rhs )

        elif isinstance( instr, Call):
            name = instr.name
            

        yield current_set.copy()
