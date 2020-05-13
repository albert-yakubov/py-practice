def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dequeue = []
    ans = []

    for i in range(k):
        while dequeue and dequeue[-1][0] < nums[i]:
            dequeue.pop()

        dequeue.append((nums[i], i))

    for i in range(k, len(nums)):
        ans.append(dequeue[0][0])
        if dequeue and (i - dequeue[0][1]) >= k:
            dequeue.pop(0)

        while dequeue and dequeue[-1][0] < nums[i]:
            dequeue.pop()

        dequeue.append((nums[i], i))

    ans.append(dequeue[0][0])

    return ans
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(0, nums, k))

# unclear about what its actually returning(appears to be number of slides)