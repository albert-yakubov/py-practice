def product_except_self(self, nums = [1,2,3,4]):
    # get the length of an array
    length = len(nums)
    # declare left, right, answer
    L, R, answer = [0]* length, [0]* length, [0]* length
    # product of elements to left
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i-1] * L[i-1]
    # product of element to the right
    R[length - 1] = 1 
    for i in reversed(range(length -1)):
        R[i] = nums[i + 1] * R[i + 1]
    #now the answer
    for i in range(length):
        answer[i] = L[i] * R[i]
    return answer
    
# test:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
nums = [1,2,3,4]
print(product_except_self(nums))