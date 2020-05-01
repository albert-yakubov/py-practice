class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if i == nums[i]:
                return i
        return i

        