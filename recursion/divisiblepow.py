# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b and 
# returns True if a is a power of b.




def isp(a,b):  
    if a%b==0 and isp(a/b,b):
        return True
    elif a/b==b:
        return True
    else:
        return False
    
x = 4
y = 2
print(isp(x, y))