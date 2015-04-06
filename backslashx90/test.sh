#!/bin/bash
os=`uname`
input="0
1
0
1
-4
-5
-2
2
65
2
-0
-9
10
11
-6
21
21
12
0
-0
90
-12
34
-43
-90
-8
-78
-9
-12
12
23
45
"

red=$(echo -ne '\e[01;31m')
green=$(echo -ne '\e[01;32m')
cyan=$(echo -ne '\e[01;34m')
nc=$(echo -ne '\e[00;0m')

args=''

function infarand {
    while true; do
        echo $RANDOM
    done
}

input="$input $(head -n 1000 <(infarand))"

passed=0
failed=0
function run_test {
    i=$1
    in_file=$(echo $i | sed 's/py$/in/g')
    real_input=$([ -f $in_file ] && cat $in_file || echo -e $input)
    real="$(echo -e "$real_input" | python2 $i)"
    if [ $? -ne 0 ] ; then
        echo "${red}$i: Bad test. Python fails${nc}"
        echo "$real"
    else
        echo -n "${nc}"
        python2 compile.py -o /tmp/$$test.s $args $i && \
            gcc -m32 -o/tmp/$$test /tmp/$$test.s runtime/libruntime.a -lm
        rc=$?
        echo -n "$green|$nc ${cyan}$(printf '%-50s' $i) ["
        if [ $rc -ne 0 ] ; then
            echo "${red}FAIL${nc}]"
            failed=$(($failed + 1))
            cat $i | while read lin ; do
                        echo " + " "$lin"
                     done
        else
            this="$(echo -e "$real_input" | /tmp/$$test)"
    
            diff <(echo $this) <(echo $real) > /dev/null
    
            if [ $? -eq 0 ] ; then
                echo "${cyan}PASS${cyan}] $green|"  
                passed=$(($passed + 1))
            else
                echo "${red}FAIL${cyan}] $green|"  
                failed=$(($failed + 1))
                echo " + Expected:"
                echo $real | while read line 
                        do echo " + + $line"
                    done
                echo " + Got:"
                echo $this | while read line 
                        do echo " + + $line"
                    done
            fi
    
            rm /tmp/$$test*
        fi
    fi
}

while [ $1 ] ; do
    
    case $1 in
        -d) args="$args -d"
        ;;
        -t) 
            shift
            run_test $1
            exit 0
        ;;
    esac
    shift
done
    

for test_set in tests old_tests secret_tests ; do
    printf "$green+-------------------[ %-13s ]-----------------------+$nc\n" $test_set
    tests=$(find $test_set -name '*.py' | sort)

    for i in $tests ; do
        run_test $i
    done
    echo -ne "${nc}"
done

printf "$green+-----------------------------------------------------------+$nc\n" $test_set
printf "$green|                     Passed: $passed/$(($passed + $failed))                       |$nc\n"
printf "$green+-----------------------------------------------------------+$nc\n" $test_set

