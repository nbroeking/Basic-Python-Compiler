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
	gcc -m32 -o $@ -c $<
