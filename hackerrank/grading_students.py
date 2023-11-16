#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    a = 0
    for i in grades:
        # Write your code here
        gap_value = 5 - math.fmod(i, 5)
        if i < 38:
            pass 
        elif gap_value <3:
            grades[a] = int(i + gap_value)
        else:  pass
        a += 1
    return grades

        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    print('\n'.join(map(str, result)))
    #print('\n')

    #fptr.close()
