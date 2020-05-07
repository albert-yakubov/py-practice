import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    flag =0
    str1="Too chaotic"
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            flag=1
    for j in range(max(0,val-2), pos):
        if q[j] > val:
            moves+=1
    if(flag==0):
        print(moves)
    else:
        print(str1)