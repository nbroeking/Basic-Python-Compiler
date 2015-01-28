#!/bin/bash

cd tests

py_file=$1
in_file=${py_file/py/in}
zip_file=${py_file/py/zip}

cat > $in_file

zip -r $zip_file $1 $in_file
chmod o+r $zip_file
