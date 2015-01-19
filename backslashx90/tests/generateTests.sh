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
    echo "gcc -o test ${src[$i]}">&3
    echo "./test > file1">&3
    echo "python ${src[$i]} > file2">&3
    echo "diff file1 file2">&3
    echo 'if '\$''\?''>&3
    echo "${src[$i]}: passed">&3
    echo -e "\n">&3
done

exec 3>&-
chmod +x runTests
