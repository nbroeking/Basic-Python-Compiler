import os
import time

runtimes = {}

times = []

for root, _, files in os.walk('final_tests/'):
    for f in files:
        if f.endswith('.py'):
            print ("Compiling \x1b[01;32m%s\x1b[00;0m" % f)
            os.system('./build.sh %s/%s /tmp/testexe 2>/dev/null' % (root, f))
            print ("Running /tmp/testexe")
            start = time.time() 
            os.system('cat input.txt | /tmp/testexe > /dev/null')
            end = time.time()

            print ("Execution time: %fms" % ((end - start) * 1000.0))

            runtimes[f] = end-start


os.system('git checkout hw6')

for root, _, files in os.walk('final_tests/'):
    for f in files:
        if f.endswith('.py'):
            os.system('./build.sh %s/%s /tmp/testexe 2>/dev/null' % (root, f))
            start = time.time() 
            os.system('cat input.txt | /tmp/testexe > /dev/null')
            end = time.time()

            print ("Execution time: %fms" % ((end - start) * 1000.0))
            print ("%s %s \x1b[01;32m%f\x1b[00;0m" % (f, " " * (100 - len(f)), (end-start) - runtimes[f]))



os.system('git checkout master')

