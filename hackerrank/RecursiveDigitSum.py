#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    in_list = list(map(int, n))
    sum_num= str(sum(in_list)*k)
    n=list(sum_num)
    for i in range(k-1):
        if len(n)==1:
            break
        else:
            in_list = list(map(int, n))
            sum_num= str(sum(in_list))
            n=list(sum_num)

    return int(sum_num)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(str(result) + '\n')

