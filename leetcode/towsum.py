def maxProfit(self, prices = []):
    #base
    if len(prices) == 0:
        return 0
    else:
        low = 99999
        profitmax = 0 
        for price in prices:
            if price - low > profitmax:
                profitmax = price - low
            elif price< low:
                low = price 
        return profitmax
prices = [999, 888, 777, 555, 10000]

print(maxProfit(prices))