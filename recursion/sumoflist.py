def recurse_list_sum( data_list ):
    total = 0
    for element in data_list: 
        if type(element) == type([]):
            total = total + recurse_list_sum(element)
        else:
            total = total + element
    
    return total

arr = [1, 2, [3,4],[5,6]]
print(recurse_list_sum(arr))