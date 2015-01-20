#Not a normal make file
#Written By: Nic Broeking

test: ; cd runtime && make ; cd ../tests && ./generateTests.sh


.PHONY: package
package:
	mkdir -p package
	cp *.py package/
	cp runtime/*.{c,h} package
	cd package && zip -r ../package.zip *

clean: ; cd runtime && make clean; rm *.pyc ; cd .. ; rm tests/*.to ; rm tests/*.s ; rm tests/file* ; rm package.zip ; rm tests/tester
