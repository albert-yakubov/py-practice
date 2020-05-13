def whatFlavors(cost, money):
    dict_flavor = {}
    for i, price in enumerate(cost):
        if (money -  price) in dict_flavor:
            print(str(dict_flavor[money - price]+1) + ' ' + str(i+1))
            return
        else:
            dict_flavor[price] = i


# MY TEST SCRIPT
cost = [5, 5, 3, 4, 4]
money = 8

print(whatFlavors(cost, money))