def contains_duplicate(self, nums = []):
    
    if len(set(nums)) < len(nums):
        return True  
    else:
        return False

nums = [2,3,4,5,6,7,8]
nums2 = [2,3,4,5,6,7,8, 2,3,4,5,6,7,8]

print(contains_duplicate(nums))
print(contains_duplicate(nums2))
