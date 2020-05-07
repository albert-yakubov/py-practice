arr = [2, 4, 1, 6, 12, 4, 7]
sum = 14
def sumExits(self, sum, arr=[]):
    # if(arr==null|| arr.length < 3{return false}
    if arr is None and arr.lenght < 3:
        return False
    for i in arr.length:
        remainder = sum - arr[i]
        if sumOfTwoExits(arr, remainder):
            return True
    return False

print(sumExits(0, arr, sum))




def sumOfTwoExits(self, arr, sum, indexToIgnore):
    pass