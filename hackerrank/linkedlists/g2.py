def mergeSortArray(self, arr=[], arr2=[]):
    arr3 = []
    for i in arr:

        arr3.append(i)
    for j in arr2:
        arr3.append(j)
    arr3.sort()
    return arr3

arr = [1, 2, 3, 4, 5, 6]
arr2 = [7, 8, 9, 10]
print(mergeSortArray(0, arr, arr2))