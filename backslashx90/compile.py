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

    if len(argv) != 2:
        print("Usage: python compiler.py <file>")
        sys.exit()
    ast = comp.parseFile(argv[1])
    print("Original: ")
    print(ast)
    
    flattened = stage1.flatten(ast)
    print("\nFlattened:")
    for i in flattened:
        print(i._to_str())

    newname = argv[1]
    if newname.endswith('.py'):
        newname=newname[:-3]+".s"
    stage2.stage2(flattened, newname);
    

if __name__ == "__main__":
    main(sys.argv)
