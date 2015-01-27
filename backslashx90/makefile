#Not a normal make file
#Written By: Nic Broeking

TEST_FLAGS?=

test: ; cd runtime && make ; cd .. ; ./test.sh $(TEST_FLAGS)
.PHONY: package test
package:
	mkdir -p package
	cp *.py package/
	cp runtime/*.c package
	cp runtime/*.h package
	cd package && zip -r ../package.zip *

clean: ; cd runtime && make clean; cd .. ;rm *.pyc ; rm tests/*.s ; rm tests/file* ; rm package.zip ; rm tests/tester ; rm tests/test
