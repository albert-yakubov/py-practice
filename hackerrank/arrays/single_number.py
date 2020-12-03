# find a digit that only appears once
from typing import List


def singleNumber(self, nums: List[int]) -> int:
    visitedNums = {}
    for index in nums:
        if index in visitedNums:
            visitedNums[index] += 1
        else:
            visitedNums[index] = 1
    for indexInVisited in visitedNums:
        if visitedNums[indexInVisited] == 1:
            return indexInVisited

# XOR association method XOR guarantees each num appears twice
# except for one
# very clever approach
def singleNumberAgain(self, nums: List[int]) -> int:
    current_num = nums[0]
    for num in nums[1:]:
        current_num = current_num ^ num
        #print(current_num)
        return current_num
    return current_num


testArray = [1, 2, 1, 2, 1, 2, 3]
print(singleNumber(0, testArray))
print(singleNumberAgain(0, testArray))