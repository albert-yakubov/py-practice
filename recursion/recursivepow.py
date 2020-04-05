def pow(a, b):
    if b==0:
        return 1
    if a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a*pow(a, b-1)
    
print(pow(3,4))