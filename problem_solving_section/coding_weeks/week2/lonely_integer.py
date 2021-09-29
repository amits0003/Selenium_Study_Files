#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'lonelyinteger' function below.

The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY a as parameter.
"""


def lonelyinteger(a):
    temp = 0
    for ele in a:
        temp = a.count(ele)
        if temp == 1 :
            print(ele)

a_ = input("Enter the elements")

b = list(map(int, a_.split(",")))

lonelyinteger(b)