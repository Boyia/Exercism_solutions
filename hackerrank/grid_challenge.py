#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    in_list = list(map(list,grid))
    new_list=[]
    for i in in_list:
        i.sort()
        new_list.append(i)
    #print(new_list)
    
    flag = 0
    for r in range(len(new_list)-1):
        for c in range(len(new_list[0])):
            if new_list[r][c]<= new_list[r+1][c]:
                pass
            else: 
                flag = 1
                break
    if flag == 1: return("NO")
    else: return('YES')

    

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        #print(result + '\n')


