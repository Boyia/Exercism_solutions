#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #define count flag
    # neg_num = 0 
    neg_num = len(list(filter(lambda x: x < 0 , arr)))
    zero_num = len(list(filter(lambda x: x == 0 , arr)))
    pos_num = len(list(filter(lambda x: x > 0 , arr)))
    # zero_num = 0 
    # pos_num = 0
    arr_num = len(arr)
    # for i in arr:
    #     if i < 0:
    #         neg_num+=1
    #     elif i == 0:
    #         zero_num+=1
    #     elif i > 0:
    #         pos_num+=1
    print(float(pos_num/arr_num))
    print(float(neg_num/arr_num))
    print(float(zero_num/arr_num))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
