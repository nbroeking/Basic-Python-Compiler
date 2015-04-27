import os
import time

totalrt = 0

times = []
diffs = []

os.system('make -f mk notests')
for root, _, files in os.walk('final_tests/'):
    for f in files:
        if f.endswith('.py'):
            print ("Compiling \x1b[01;32m%s\x1b[00;0m" % f)
            os.system('./build.sh %s/%s /tmp/testexe 2>/dev/null' % (root, f))
            print ("Running /tmp/testexe")
            start = time.time() 
            os.system('/tmp/testexe < input.txt > /dev/null')
            end = time.time()

            print ("Execution time: %fms" % ((end - start) * 1000.0))

            totalrt += end-start


print "Total " + str(totalrt)
