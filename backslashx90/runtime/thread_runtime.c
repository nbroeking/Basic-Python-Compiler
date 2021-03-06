
#include <pthread.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>

#include "runtime.h"

#include <assert.h>

typedef unsigned long u32_t;
typedef long s32_t;

struct thread_args {
    big_pyobj* fn; /* function to call */
    pyobj* into; /* return value */
    int* args; /* arg list */
    int nargs; /* number of args */
};


extern void* __thread_start(void*);

pthread_t dispatch(u32_t* retval, big_pyobj* fn, int arg_count, ...) {
    pthread_t thread;
    struct thread_args* args = malloc(sizeof(struct thread_args));
    assert(args);

    args->fn = fn;
    args->into = (s32_t*)retval;
    args->args = malloc(sizeof(u32_t)*arg_count);
    assert(args->args);
    args->nargs = arg_count;

    va_list l;
    va_start(l, arg_count);
    int i;
    for(i = 0; i < arg_count; ++ i) {
        args->args[i] = va_arg(l, u32_t);
    }

    if(fn->u.f.flags == 1) {
        pthread_create(&thread, NULL, __thread_start, args);
        // fprintf(stderr, "Starting a new thread %lu\n", (unsigned long)thread);
        return thread;
    } else {
     if(fn->u.f.flags != 0) {
        /* conditionally pure. Check the conditions */
        int b = fn->u.f.flags >> 1;
        pyobj* ptr = (pyobj*)args->args;
        while(b) {
            big_pyobj* ptra3 = (big_pyobj*)(*ptr & (~0x03));
            if(b & 1) {
                if((*ptr & 0x3) == 0x3 &&
                    ptra3->tag == FUN &&
                    ptra3->u.f.flags == 1);
                else {
                    // fprintf(stderr, "Conditionally pure false\n");
                    __thread_start(args);
                    return 0;
                }
                ptr ++;
            }
            b >>= 1;
        }

        /* Conditional purity is true. So we can spawn a thread */
        pthread_create(&thread, NULL, __thread_start, args);
        // fprintf(stderr, "Conditionally pure thread %lu\n", (unsigned long)thread);
        return thread;
     }
     // fprintf(stderr, "Not pure\n");
     /* run synchronously if impure */
     __thread_start(args);
     free(args);
     return 0;
    }
}

void join_thread(pthread_t p) {
    if(p == 0) {
        return;
    }
    pthread_join(p, NULL);
    // fprintf(stderr, "Join thread %lu\n", (unsigned long)p);
}

