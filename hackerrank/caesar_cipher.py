#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    new_list=[]
    for i in s:
        old_position =  ord(i)
        #need to mention k is more than 26
        if k>26:
            k = int(math.fmod(k, 26))
        if i.isalpha() == False:
            new_letter = i
        elif (old_position <=90 and old_position + k > 90) or  (old_position in range(97,123) and old_position + k > 122):
            new_letter = chr(ord(i) + k - 26)
        else:
            new_letter = chr(ord(i) + k)
        new_list.append(new_letter)
        ##
        # elif (old_position <=90 and old_position + k > 90):
        #     actual_change = k//26 + 1
        #     new_letter = chr(ord(i) + k - actual_change*26)
        # elif (old_position in range(97,123) and old_position + k >= 122):
        #     actual_change = k//26 
        #     new_letter = chr(ord(i) + k - actual_change*26)
        # else:
        #     new_letter = chr(ord(i) + k)
    trans_list =''.join(new_list)
    return trans_list
    

    

if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print (result)
