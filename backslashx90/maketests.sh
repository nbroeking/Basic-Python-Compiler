files=$(find tests -name '*.py' -and -not -name 'onsite*')

for i in $files ; do
    infile=$(echo $i | sed 's/py$/in/')
    if [ ! -e $infile ] ; then
        echo -e '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17' > $infile
    fi
done

cd tests
zipfiles=$(find . -name '*.in' -or -name '*.py' -and -not -name 'onsite*')
zip -r ../tests.zip $zipfiles

chmod o+r ../tests.zip
