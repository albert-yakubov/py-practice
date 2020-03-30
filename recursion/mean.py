# total elements of an array

# M = sum of all elements / by # of elements
def findMean(A, N):
    # base
    # number
    if N==1:
        # if number is nothing then return nothing
        return A[N-1]
    else:
        return ((findMean(A, N-1)*(N-1)*A[N-1])/ N)

A = [1,2,3,4,7,5,6,4,5,6,1,3]
N = len(A)
print (findMean(A, N))