#stage0
#Written By: Nic and Josh

#This is the parser module 

import sys
import compiler.ast as ast

class WTFException(Exception):
    def __init__(self, s):
        super(self, Exception).__init__(s)

class Identifier:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "[Ident %s]" % self.name

class Digits:
    def __init__(self, name):
        self.digits = name
    def __repr__(self):
        return "[Digits %s]" % self.digits

class Operator:
    def __init__(self, name):
        self.operator = name
    def __repr__(self):
        return "[Op %s]" % self.operator

def parseFile(name):
    stage = Stage0(name)
    tokens = stage.tokenize()
    return stage.parse(tokens)

class Stage0:
    def __init__(self, filename):
        self.f = open(filename)       

    def tokenize(self):
        tmpLines = self.f.read().splitlines()
        lines = []
        for x in tmpLines:
            parts = x.split(";")
            if x != "":
                lines += parts
            
        #Clear all spaces
        lines = [x.strip(' \r\n\t') for x in lines]
    
        print("STAGE1")
        for y in lines:
            print(y)

        tokens = self._tokenize2( lines ) # retunr [[String]]
        for i in tokens:
            print i
            
        return tokens

    def _tokenize2(self, lines):
        return [self.tokenizeline(x) for x in lines]
        
    def tokenizeline(self, line):
        buf = []
        i = 0
        while i < len(line):
            start = i
            if line[i].isalpha():
                while i < len(line) and (line[i].isalpha() or line[i].isdigit()):
                    i += 1
                buf.append(Identifier(line[start:i]))

            elif line[i].isdigit():
                while i < len(line) and line[i].isdigit():
                    i += 1
                buf.append(Digits(line[start:i]))

            elif line[i].isspace():
                while i < len(line) and line[i].isspace():
                    i += 1

            elif not line[i].isalpha() and not line[i].isdigit():
                i += 1
                buf.append(Operator(line[start:i]))

            else:
                raise Exception("WTFException")

                    
        return buf
                
    
    def parse(self, tokens):
        buf = []
        for i in tokens:
            buf.append( self._parse(i) )
        return ast.Module(None,  \
                    ast.Stmt( buf ))

    def is_open_paren(self,op):
        return isinstance(op, Operator) and op.operator == '('

    def is_close_paren(self,op):
        return isinstance(op, Operator) and op.operator == ')'

    def next_token(self, tokens, i):
        # skip parens if they are there
        cnt = 0
        if self.is_close_paren(tokens[i]):
            cnt = 1

        i -= 1
        while cnt != 0:
            if self.is_close_paren(tokens[i]):
                cnt += 1
            elif self.is_open_paren(tokens[i]):
                cnt -= 1
            i -= 1
        return i

    def strip_paren(self, tokens):
        while self.is_open_paren(tokens[0]) and \
                self.is_close_paren(tokens[-1]):
                tokens = tokens[1:-1]
        return tokens

    def _parse(self, tokens):
        print "TOKENS", tokens

        tokens = self.strip_paren(tokens)
        if len(tokens) == 1:
            # base case
            if isinstance(tokens[0], Operator):
                raise WTFException("Operator not expected %s" % tokens[0])
            elif isinstance(tokens[0], Identifier):
                return ast.Name(tokens[0].name)
            elif isinstance(tokens[0], Digits):
                return ast.Const(int(tokens[0].digits))

        if isinstance(tokens[0], Identifier):
            if tokens[0].name == 'print':
                return ast.Printnl([self._parse(tokens[1:])], None)
        else:
            # first thing, find operator=
            i = len(tokens) - 1 
            while i >= 0:
                if isinstance(tokens[i], Operator):
                    if tokens[i].operator == '=':
                        lhs = self._parse(tokens[0:i-1])
                        rhs = self._parse(tokens[i+1:])
                        if not isinstance(lhs, ast.Name):
                            raise WTFException("Expected identifier")
                        return ast.Assign([ast.AssName(lhs.name, OP_ASSIGN)], _parse(rhs))
                i = self.next_token(tokens, i)
        
            # first thing, find operator+
            i = len(tokens) - 1 
            while i >= 0:
                print "Python sux", tokens[i]
                if isinstance(tokens[i], Operator):
                    if tokens[i].operator == '+':
                        lhs = self._parse(tokens[0:i])
                        rhs = self._parse(tokens[i+1:])
                        return ast.Add((lhs, rhs))
                i = self.next_token(tokens, i)

            # first thing, find operator-
            i = len(tokens) - 1 
            while i >= 0:
                if isinstance(tokens[i], Operator):
                    if tokens[i].operator == '-':
                        rhs = self._parse(tokens[i+1:])
                        return ast.UnarySub(rhs)
                i = self.next_token(tokens, i)

            # first thing, find operator(
            i = len(tokens) - 1 
            while i < len(tokens):
                if isinstance(tokens[i], Operator):
                    lhs = self._parse(tokens[0:i-1])
                    return ast.CallFunc(lhs, [])
                i = self.next_token(tokens, i)

