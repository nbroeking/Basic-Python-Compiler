#!/usr/bin/python
# Main Python Module
# Written By Nicolas Broeking and Josh Rahm
# Team: x90

import printer
import compiler.ast as pyast
import compiler as comp
import stage1 as flat
import stage2 as reg
import viper.core as core
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
    flattened = flat.flatten(ast)
    for n in flattened:
        print(n._to_str())

#Register Allocation
    tree = reg.selection(flattened);

#Print the ASM tree to a file
    printer.output(tree, outfile)

if __name__ == "__main__":
    main(sys.argv)
