#!/bin/bash
people=$(curl http://csci4555.cs.colorado.edu/uploads/tests/ | perl -n -e '/.*href="(\w*).*"/ && print "$1\n"')

for i in $people ; do
    test=$(curl -f http://csci4555.cs.colorado.edu/uploads/tests/$i/$1 2>/dev/null)
    if [[ $? -eq 0 ]] ; then
        echo "Found test at $i"
        echo "$test" > dumped_test.py
        exit 0
    fi
done

echo "No test found"
exit 1
