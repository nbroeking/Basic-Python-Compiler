#!/usr/bin/python
# Main Python Module
# Written By Nicolas Broeking and Josh Rahm
# Team: x90

import printer
import function_comb as preproc
import compiler.ast as pyast
import compiler as comp
import stage1 as flat
import stage2 as reg
from declassify import declassify


try:
    import viper.core as core
except:
    import core as core

import sys

def main( argv):

    outfile = None
    debug = False

    i = 1

#Set debug mode if debug mode is flagged
    while argv[i].startswith('-'):
        if argv[i] == '-o':
            outfile = argv[i+1]
            i += 1
        if argv[i] == '-d':
            debug = True

        i += 1
    if not debug:
        sys.stdout = sys.stderr # open('/dev/null', 'w')
            
#Check arguments
    if len(argv) < 2:
        print("Usage: python compiler.py <file>")
        sys.exit()

#If in debug write all stdout to stderr
    sys.stderr.write(open(argv[i],'r').read())

    ast = comp.parseFile(argv[i])
    print ast

#Get the outfile from arguments
    if outfile is None:
        outfile = argv[i]
        if outfile.endswith('.py'):
            outfile=outfile[:-3]+".s"

#Flatten
    # defs :: [DefinedFunction]
    defs = preproc.preprocess_functions(ast)
    defsmap = dict([(i.name,i) for i in defs])


    print "\n-------- Before declassify --------------"
    for fn in defs:
        print "AST: ", fn.pyast
    for fn in defs:
        new_ast = declassify(fn.get_ast())
        fn.set_ast(new_ast)


    print "\n-------- Function Defs --------------"
    for fn in defs:
        print "AST: ", fn.pyast

    print "\n--------------------------\n"
    for fn in defs:
        flattened = flat.flatten(fn.get_ast(), True)
        fn.set_ast(flattened)

        print "Fattened: %s (%s) {" % (fn.name, fn.parent_closure)
        for i in flattened:
            print "    " + str(i)
        print "}\n"

#Register Allocation

    global_data_section = {}
    for fn in defs:
        print "--------", fn.name, "----------"
        (data_section, tree) = reg.selection(fn.get_ast(), defsmap, fn.name);
        global_data_section.update(data_section)
        fn.set_ast(tree)

    total = []
    for fn in defs:
        total += fn.build_final_asm_tree()
#Print the ASM tree to a file
    printer.output(total, outfile, len(defsmap[preproc.mangle("","main")].parent_closure), global_data_section)

if __name__ == "__main__":
    main(sys.argv)
