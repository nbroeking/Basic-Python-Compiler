#Not a normal make file
#Written By: Nic Broeking

test: ; cd runtime && make ; cd ../tests && ./generateTests.sh && ./runTests

.PHONY: package
package:
	mkdir -p package
	cp *.py package/
	cp runtime/*.{c,h} package
	cd package && zip -r ../package.zip *

clean: ; cd runtime && make clean; cd .. ;rm *.pyc ; rm tests/*.s ; rm tests/file* ; rm package.zip ; rm tests/tester ; rm tests/test
