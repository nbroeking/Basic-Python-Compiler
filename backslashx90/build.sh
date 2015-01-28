#!/bin/bash

python2 compile.py -o /tmp/test.s $1
gcc -m32 -o $2 /tmp/test.s runtime/libruntime.a -lm
