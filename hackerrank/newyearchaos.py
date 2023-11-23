#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#ls

def minimumBribes(q):
    # Write your code here
    origin_q =[ x+1 for x in range(len(q))]
    bribes = 0
    flag=0
    for i in range(len(q)):
        right_cnt= origin_q.index(q[i])
        if right_cnt - i>2:
            flag=1
            break
        while(q[i]>origin_q[i]):
            #change position
            origin_q[right_cnt],origin_q[right_cnt-1] = origin_q[right_cnt-1],origin_q[right_cnt]
            right_cnt -=1
            bribes += 1
    if flag == 1:
        print("Too chaotic")
    else:
        print(bribes)



        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
