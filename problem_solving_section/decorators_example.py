"""
First Class Functions
"""


def ret_capital(text):
    return text.upper()


print(ret_capital('This Sentence will get printed in capital letters'))

cap_letter = ret_capital

print(cap_letter('hello'))


def ret_lower(text):
    return text.lower()


def display_func(func):
    display_message = func('This line created from function passes as an argument')
    print(display_message)


display_func(ret_capital)
display_func(ret_lower)


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


def display_inside_value():
    print('Hi this is inside value')


display_inside_value = print_value(display_inside_value)

display_inside_value()

print('----------------2nd part--------------------')

import time
import math


def decorator_function(func):
    def new_function(*args, **kwargs):
        begin = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("Total time taken in : ", func.__name__, end - begin)

    return new_function


