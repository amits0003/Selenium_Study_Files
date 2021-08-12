#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice = []
    bob = []
    final_res = []
    for indexA, value in enumerate(a):
        if value < b[indexA]:
            alice.append(1)
        elif value > b[indexA]:
            bob.append(1)
        elif value == b[indexA]:
            pass

    if len(bob) > 0 or len(alice) > 0:
        temp = 0
        for element, value in bob:
            temp = temp + element
        final_res.append(temp)
        temp2 = 0
        for element in alice:
            temp = temp + element

        final_res.append(temp)

    print(final_res)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = list(map(int, input().rstrip().split()))

    #b = list(map(int, input().rstrip().split()))
    a = [5,5,5]
    b = [5,5,5]

    result = compareTriplets(a, b)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
