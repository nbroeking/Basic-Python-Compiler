#!/usr/bin/python
# Main Python Module
# Written By Nicolas Broeking and Josh Rahm
# Team: x90

import compiler.ast as pyast
import compiler as comp
import stage1
import stage2
import core
import sys

def main( argv):

    outfile = None
    debug = False

    i = 1

    while argv[i].startswith('-'):
        if argv[i] == '-o':
            outfile = argv[i+1]
            i += 1
        if argv[i] == '-d':
            debug = True

        i += 1
    if not debug:
        sys.stdout = sys.stderr # open('/dev/null', 'w')
            

    if len(argv) < 2:
        print("Usage: python compiler.py <file>")
        sys.exit()
    # print("Original: ")
    # print(ast)
    
    sys.stderr.write(open(argv[i],'r').read())
    ast = comp.parseFile(argv[i])
    print ast

    flattened = stage1.flatten(ast)
    # print("\nFlattened:")
    # for i in flattened:
    #     print(i._to_str())

    if outfile is None:
        outfile = argv[i]
        if outfile.endswith('.py'):
            outfile=outfile[:-3]+".s"

    stage2.stage2(flattened, outfile);
    

if __name__ == "__main__":
    main(sys.argv)
