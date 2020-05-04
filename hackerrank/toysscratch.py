def toys(toy_prices, dollars):
    toy_prices = [1,2,3,4]
    dollars = 7
    toys = 0
    toy_prices.sort()
    i = 0
    while(dollars - toy_prices[i] >= 0):
        dollars = dollars - toy_prices[i]
        i += 1

 
            
    return  i

tp = [1,2,3,4]
S = 7
print(toys(tp, S))     
