input = [51590, 53619, 101381,81994]

from typing import List

def func(xs: List[int])-> int:
#take the mass and devide by 3 round down and subtract two
    ys = list()
    for x in xs:
        x = x//3
        ys.append(x-2)
    return sum(ys)
    
# this is one liner:
def fun2(xs: List[int])-> int:
    return sum(y-2 for y in (x//3 for x in xs))
    
print(func(input))
print(fun2(input))