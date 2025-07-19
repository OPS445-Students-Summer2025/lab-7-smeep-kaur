#!/usr/bin/env python3
# Student ID: smeep-kaur

def function1():
    a = 'object_function1'
    print('print() call in function1 on a:', a)

def function2():
    a = 'function2_object'
    print('print() call in function2 on a:', a)

a = 'object_in_main'
print('print() call in main on a:', a)
function1()
print('print() call in main on a:', a)
function2()
print('print() call in main on a:', a)
