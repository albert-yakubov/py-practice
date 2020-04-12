def recurse_list_sum( data_list ):
    total = 0
    for element in data_list: 
        if type(element) == type([]):
            total = total + recurse_list_sum(element)
        else:
            total = total + element
    
    return total

arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
print(recurse_list_sum(arr))