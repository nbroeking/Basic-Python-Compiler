OBS= \
    hashtable.o \
    hashtable_itr.o \
    hashtable_utility.o \
    runtime.o

all: $(OBS)
	ar -rcs libruntime.a $(OBS)

clean:
	-rm *.a
	-rm *.o

%.o:%.c
	gcc -g3 -ggdb -m32 -o $@ -c $<
