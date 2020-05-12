

def peekIndexMountainArray(self, A):
    # for index in range(len(A) - 1):
    #     if A[index] > A[index + 1]:
    #         return index
    #     return 0

    # binary search improvement:
    # keep lower and higher values

    lower = 0
    higher = len(A) - 1
    while lower < higher:
        middle = (lower + higher) // 2
        # then binary search:
        if A[middle] > A[middle + 1]:
            return middle
        lower = middle
    return lower