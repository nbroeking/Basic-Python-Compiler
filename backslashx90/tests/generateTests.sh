#!/bin/bash

src=()

for i in $(find . | egrep '.*\.py?$') ; do
    src[$cnt]=$i
    cnt=$[cnt + 1]
done

# remove the testFile if it exists
rm -f ./runTests || true

# open testscript
exec 3<> ./runTests

os=`uname`

# some commonly used files to generate
echo '#!/bin/bash'>&3
echo 'echo '\''Running the test suit how did you do?'\'''>&3
echo -e "\n">&3
# iterate through all of the tests and 
# run them
for ((i=0;i<${#src[@]};i++)) ; do
    echo "echo \"Running Test: ${src[$i]}\"">&3
    echo "gcc -m32 -otest ${src[$i]} ../runtime/libruntime.a -lm">&3
    echo "echo 10 1 -5 -2 2 65 2 -0 -9 10 | ./test > file1">&3
    echo "echo 10 1 -5 -2 2 65 2 -0 -9 10 | python ${src[$i]} > file2">&3
    echo "diff file1 file2 > file3">&3
    echo 'if '\$''\?''>&3
    echo "\t${src[$i]}: passed">&3
    echo 'elif'>&3
    echo '\t echo failed'>&3
    echo 'fi'>&3
    echo -e "\n">&3
done

exec 3>&-
chmod +x runTests
