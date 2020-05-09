import math
import os
import random
import re
import sys

# Complete the boardCutting function below.
def boardCutting(cost_y, cost_x):
    m=len(cost_y) -1
    n=len(cost_x) -1
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)
    xSeg = 1
    ySeg = 1
    i=0
    j=0
    cost=0
    temp=0
    while(xSeg<=m+1 and ySeg<=n+1):
        if i<=m and j<=n:
            if cost_y[i]>=cost_x[j] :
                temp=cost_y[i]*ySeg
                cost+=temp
                xSeg+=1
                i+=1
            else:
                if j<=n:
                    temp=cost_x[j]*xSeg
                    cost+=temp
                    ySeg+=1
                    j+=1
        if i==m+1:
            while(j<=n):
                temp=cost_x[j]*xSeg
                cost+=temp
                ySeg+=1
                j+=1
        if j==n+1:
            while(i<=m):
                temp=cost_y[i]*ySeg
                cost+=temp
                xSeg+=1
                i+=1
    return cost%(10**9+7)

a = [2, 2]
b = [1, 1]
print(boardCutting(a, b))
c = [4, 4]
d = [1, 1]
print(boardCutting(c, d))