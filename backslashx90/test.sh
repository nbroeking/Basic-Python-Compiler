#!/bin/bash
os=`uname`
input="10
1
-5
-2
2
65
2
-0
-9
10"

red=$(echo -ne '\e[01;31m')
green=$(echo -ne '\e[01;32m')
cyan=$(echo -ne '\e[01;36m')
nc=$(echo -ne '\e[00;0m')

args=''
tests=$(find tests -name '*.py' | sort)
while [ $1 ] ; do
    
    case $1 in
        -d) args="$args -d"
        ;;
        -t) 
            shift
            tests=$1
        ;;
    esac
    shift
done

for i in $tests ; do
    real="$(echo -e "$input" | python2 $i)"
    if [ $? -ne 0 ] ; then
        echo "${red}Bad test. Python fails${nc}"
        echo "$real"
    else
        echo -n "${nc}"
        python2 compile.py -o /tmp/$$test.s $args $i && \
            gcc -m32 -o/tmp/$$test /tmp/$$test.s runtime/libruntime.a -lm
        rc=$?
        echo -n "${cyan}$(printf '%-50s' $i) ["
        if [ $rc -ne 0 ] ; then
            echo "${red}FAIL${nc}]"
            cat $i | while read lin ; do
                        echo " + " $lin
                     done
        else
            this="$(echo -e "$input" | /tmp/$$test)"
    
            diff <(echo $this) <(echo $real) > /dev/null
    
            if [ $? -eq 0 ] ; then
                echo "${green}PASS${cyan}]"  
            else
                echo "${red}FAIL${cyan}]"  
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

done
echo -ne "${nc}"

