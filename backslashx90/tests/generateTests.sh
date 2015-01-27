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
echo "red=\$(echo -ne '\\e[01;31m')">&3
echo "green=\$(echo -ne '\\e[01;32m')">&3
echo "cyan=\$(echo -ne '\\e[01;36m')">&3
echo "nc=\$(echo -ne ' \\e[00;0m')">&3
echo 'echo -e '\"'\n${cyan}Running the test suit how did you do? ${nc}'\"''>&3
echo -e "\n">&3
# iterate through all of the tests and 
# run them
for ((i=0;i<${#src[@]};i++)) ; do
    echo "echo \" \${cyan}Running Test: $i \${nc} \"">&3
    echo "python2 ../compile.py -o tester.s ${src[$i]} > file1">&3
    echo "gcc -m32 -otest tester.s ../runtime/libruntime.a -lm > file2">&3
    echo "echo 10 1 -5 -2 2 65 2 -0 -9 10 | ./test >> file1">&3
    echo "echo 10 1 -5 -2 2 65 2 -0 -9 10 | python2 ${src[$i]} >> file2">&3
    echo "diff file1 file2 > file3">&3
    echo 'if [ '\$''\?' == 0 ] '>&3
    echo 'then'>&3
    echo "    printf '  %-10s: %10s\n' \"\${green}${src[$i]}\" \"[PASS] \${nc}\" ">&3
    echo 'else'>&3
    echo "    printf '  %-10s: %10s\n' \"\${red}${src[$i]}\" \"[FAIL] \${nc}\" ">&3
    echo "    echo \"We got: \" ">&3
    echo "    cat file1">&3
    echo "    echo \"Should be: \" ">&3
    echo "    cat file2">&3
    echo "    echo -e"\n"">&3
    
    echo 'fi'>&3
    echo 'echo -e "\n"'>&3
    echo -e "\n">&3
done

exec 3>&-
chmod +x runTests
