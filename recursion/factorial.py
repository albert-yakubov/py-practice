# find factorial of log N

# calculate N then find its log value
import math
def factorial(n):
    # base
    if n == 1:
        return 0
    else:
        return factorial(n-1) + math.log(n)
    
N = 3
print (factorial(N))

# take the sum of log N value 