#!/bin/python3

import math
import os
import random
import re
import sys
"""
Complete the 'countApplesAndOranges' function below.

The function accepts following parameters:
 1. INTEGER s
 2. INTEGER t
 3. INTEGER a
 4. INTEGER b
 5. INTEGER_ARRAY apples
 6. INTEGER_ARRAY oranges
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """modified location of apples"""
    '''method 1 '''
    apple_location = [a+apple for apple in apples]
    orange_location = [b+orange for orange in oranges]

    fruit_in_range = []
    count_apple = 0
    count_orange = 0

    for idx in range(s,t+1):
        if idx in apple_location:
            count_apple+=1

        if idx in orange_location:
            count_orange+=1

    fruit_in_range.append(count_apple)
    fruit_in_range.append(count_orange)

    for ele in fruit_in_range:
        print(ele)

    '''method 2'''
    print(sum([1 for apple  in apples if (a+apple) >= s and (a+apple) <= t]))
    print(sum([1 for orange in oranges if (b+ orange) >= s and (b+ orange) <= t]))

if __name__ == '__main__':
    first_multiple_input = input("enter s and t").rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input("enter a and b").rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input("enter m and n").rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input("enter coordinates of apple").rstrip().split()))

    oranges = list(map(int, input('enter coordinates of oranges ').rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
