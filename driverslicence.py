# how long will it take me to get my license
# 20 min a visit per person
# 3 people ahead of me
# blocker: they re being calleb by name 
def waitTime(p):
    t = 20
    a = 2 
    p = 4 
    if p ==0:
       return 20  
    else:
        p = (p * t) / a
        return int(p)
    
p = 4
t = 20
a = 2 
print(waitTime(p))