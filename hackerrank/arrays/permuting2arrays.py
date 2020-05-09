def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for x in range(len(A)):
        if( A[x] + B[x] < k ):
            return "NO"

    return "YES"

k = 1
A = [1, 2, 2, 1]
B = [3, 3, 3, 4]
print(twoArrays(k,A,B))
k = 2
C = [2, 1, 3]
D = [7, 8, 9]
print(twoArrays(k,C,D))