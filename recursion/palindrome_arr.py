# check if array is palindrome

# if an array has one element then return o
def pal(arr, x, y):

    if x > y:
        return 1
    if arr[x] == arr[y]:
        return pal(arr, x+1, y-1)
    else:
        return 0


# if begin > end return 1 
if __name__ == "__main__":
    arr1 = [ 1,2,3,4,5,4,3,2,1]

    arr2 = [2,3,4,2,3,5,2,4,5,2]
    len1 = len(arr1)
    len2 = len(arr2)
    if pal(arr1, 0, len1 -1) == 1:
        print("indeed palindrome!")
    else:
        print("Not so much a palindrome!")

arr2 = [2,3,4,2,3,5,2,4,5,2]
print(pal(arr2, 0, len(arr2) -1))
arr1 = [ 1,2,3,4,5,4,3,2,1]
print(pal(arr1, 0, len(arr1) -1))
# if the numbers at start and end are equal call the fun
# and increment start and end by 1

# if the first and last not equal return 0