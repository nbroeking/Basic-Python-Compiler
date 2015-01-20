#Not a normal make file
#Written By: Nic Broeking

test: ; cd runtime && make ; cd ../tests && ./generateTests.sh


.PHONY: package
package:
	mkdir -p package
	cp *.py package/
	cp runtime/*.{c,h} package
	cd package && zip -r ../package.zip *

clean: ; cd runtime && make clean; rm *.pyc ; rm tests/*.to ; rm tests/*.s ; rm tests/file1 ; rm tests/file2
