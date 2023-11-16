#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # get hour min sceond and AM PM
    time = s.rsplit(":")
    hour = int(time[0])
    mins = str(time[1])
    sec = str(time[-1][0:2])
    # whether is morning
    morning = s.find('AM') != -1
    evening = s.find('PM') != -1
    if evening:
        if hour < 12 :
            hourtime = str(12 + hour)
            new_time = hourtime + ":" + mins + ":" + sec
        elif hour == 12:
            hourtime = str(time[0])
            new_time = hourtime + ":" + mins + ":" + sec

    elif morning:
        if hour == 12:
            hourtime = str('00')
            new_time = hourtime + ":" + mins + ":" + sec

        elif hour < 12:
            hourtime = str(time[0])
            new_time = hourtime + ":" + mins + ":" + sec
        
    else: new_time = 'wrong input'
    return new_time
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    #
