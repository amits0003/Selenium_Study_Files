'''
First Class Functions
'''


def ret_capital(text):
    return text.upper()


print(ret_capital('sentence in captial letter'))

cap_leter = ret_capital

print(cap_leter('hello'))


def ret_lower(text):
    return text.lower()


def disp_func(func):
    dip_message = func('created from function passes as an argument')
    print(dip_message)


disp_func(ret_capital)
disp_func(ret_lower)


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))

'''
Decorators
'''


def print_value(func):
    def print1():
        print('hello line 1')
        func()

        print('last line to display')

    return print1


@print_value
def disp_value():
    print('Hi this is inside value')


disp_value()

print('------------------------------------')


def disp_value1():
    print('Hi this is inside value')


disp_value1 = print_value(disp_value1)

disp_value1()

print('----------------2nd part--------------------')

import time
import math


def decorator1(func):
    def new_function(*args, **kwargs):
        begin = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("Total time taken in : ", func.__name__, end - begin)

    return new_function


