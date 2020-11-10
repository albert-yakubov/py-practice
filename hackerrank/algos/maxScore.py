from typing import List
from functools import lru_cache

def maxScore(self, nums: List[int]) -> int:
    nums = [1] + nums + [1]
    @lru_cache(None)
    def depthFirstSearch(leftIndex, rightIndex): return rightIndex - leftIndex > 1 and max(
            nums[leftIndex] * nums[i] * nums[rightIndex] + depthFirstSearch(leftIndex, i) + depthFirstSearch(i, rightIndex) for i in range(leftIndex + 1, rightIndex)) or 0



    return depthFirstSearch(0, len(nums)-1)
list = [1,2,3,4]
print(maxScore(0, list))


