#!/bin/python3

import math
import os
import random
import re
import sys



def rotate_an_array(arr, d, n):
    # d is ammount of rotations
    # a is array
    # n are the numbers starting rotation from
    
    # Function to left rotate arr[] of size n by d*/ 
    for i in range(d):
       left_rotate_by_one(arr, n)
# Function to left Rotate arr[] of size n by 1*/  
def left_rotate_by_one(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]        
    arr[n-1] = temp 
def printArray(arr, size): 
    for i in range(size): 
        print("%d"%arr[i], end =" ")

arr = [1, 2, 3, 4, 5]
d = 2
n = 5
print(rotate_an_array(arr, d, n))
print(arr)