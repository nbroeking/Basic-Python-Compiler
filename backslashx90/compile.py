# Main Python Module
# Written By Nicolas Broeking and Josh Rahm
# Team: x90

import compiler

def main():
    ast = compiler.parse('5 + 4 + input()')
    print(dir(ast))
    print(ast)
    print(getDepth(ast))


def getDepth(a_ast):
    if len(a_ast.getChildNodes()) == 0:
        return 0
    return max([getDepth(i) for i in a_ast.getChildNodes()]) + 1

if __name__ == "__main__":
    main()
