def contains_duplicate(self, nums = []):
    
    if len(set(nums)) < len(nums):
        return True  
    else:
        return False

nums = [2,3,4,5,6,7,8]
nums2 = [2,3,4,5,6,7,8, 2,3,4,5,6,7,8]

print(contains_duplicate(nums))
print(contains_duplicate(nums2))

def containsDuplicate(self, nums=[]):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # split it into two sets of numbers:
    x = len(nums)
    y = len(set(nums))
        # then check the set numbers against the given list of duplicates\
    if y < x:
            return True
        else:
            return False    
