#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # sort, sum
    arr.sort()
    min_arr = arr[:-1]
    max_arr = arr[1:]
    
    print(sum(min_arr),sum(max_arr) )
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
