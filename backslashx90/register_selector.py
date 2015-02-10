from AsmTree import Movl, Addl, Neg, Push#, Pop, Call, Subl

def allocate_registers( asm_tree ):
    # edge_list : [[string]]
    sets = list(build_interference_model( asm_tree ))
    sets.reverse()
    sets = zip(asm_tree, sets[1:])

    print ("%-20s | %s" % ("", sets[0]))
    for (i,(_,j)) in zip(asm_tree, sets[1:]):
        print ("%-20s | %s" % (i,j))
    print "----------------"

    graph = build_graph(sets)
    print_graph(graph)
    print "----------------"

    colors = color_graph( graph )
    print_graph(colors)

    #Spill Code

    #Set Names

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

            for v in l_after:
                if v != t and v != s:
                    add_interfere( ret_map, v, t )

        if isinstance( instr, Addl ):
            
            t = instr.rhs
            s = instr.lhs

            for v in l_after:
                if v != t:
                    add_interfere( ret_map, v, t )
    return ret_map


#color the graph
#map(string -> int)
def color_graph( mapping):
    ret_map = dict()

    for node in mapping:
        neighbors = mapping[node] # set
        possible = set(range(len(neighbors) + 1)) # possible registers

        for neighbor in neighbors:
            if neighbor in ret_map and ret_map[neighbor] in possible:
                possible.remove( ret_map[neighbor] )

        ret_map[node] = min(possible)

    return ret_map

def is_var(name):
    return len(name) > 0 and name[0] != '&'

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

        yield current_set.copy()
