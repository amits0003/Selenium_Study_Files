"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
long integers. """

#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    # Write your code here
    max_element = max(arr)
    min_element = min(arr)
    sum_max, sum_min = 0,0
    for ele in arr:
        if ele!=max_element:
            sum_min = sum_min+ele
    for ele in arr:
        if ele!=min_element:
            sum_max = sum_max+ele

    print(str(sum_min) + " " + str(sum_max))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
