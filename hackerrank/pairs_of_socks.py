#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # color doesnt matter here because to make a pair of socks you only need two socks
    # same answer goes for same color socks
    # iniate count
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i < n:
        # if the numbers are matching
        if ar[i]==ar[i+1]:
            #increment count 
            count = count + 1
            # of pairs so by 2
            i += 2
        else:
            i += 1
    return count

print(sockMerchant(9, [1,2,3,4,4,3,2,2,2]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()