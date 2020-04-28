def twoSum(self, nums, target):
    # dictionary for numbers that are visited 
    seen = {}
    # declare visited, i and remaining
    # then enumate through the nums and mark i and visited
    for i, visited in enumerate(nums):
        # remaining is the target minus the visited due to visited plus i should target
        remaining = target - visited
            # then add them all the new dictionary 
        if remaining in seen:
            return [seen[remaining], i]
        # mark all the nums with i
        seen[visited] = i
    # then return the dict
    return []
# self = 0
target = 9 
nums = [2,7,11,15]
print(twoSum(0, nums=nums, target=target))