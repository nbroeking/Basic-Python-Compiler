files=$(find tests -name '*.py' -and -not -name 'onsite*')

for i in $files ; do
    infile=$(echo $i | sed 's/py$/in/')
    if [ ! -e $infile ] ; then
        echo -e '0
0
2
10
1
-5
-2
2
65
2
-0
-9
10' > $infile
    fi
done

cd tests
zipfiles=$(find . -name '*.in' -or -name '*.py' -and -not -name 'onsite*')
zip -r ../tests.zip $zipfiles

chmod o+r ../tests.zip
