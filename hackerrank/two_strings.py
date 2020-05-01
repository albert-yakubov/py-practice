import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        for i in s2:
            if i in s1:
             return 'YES'
        return 'NO'
    else:    
        for i in s1:
            if i in s2:
                return 'YES'
        return 'NO'
    
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
