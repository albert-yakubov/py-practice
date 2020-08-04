from typing import List
a = [1,2,3]

def Permutation(self, nums: List[int]):
    return swapper(0, 2, 3)


a = [1,2,3]
print(a)
print(Permutation(0, a))

def findPivot(nums: List[int]):
    for num in reversed(range(1, len(nums))):
        if nums[num] < nums[num-1]:
            return num -1
    return -1

def swapPivot(nums: List[int], pivot_index: int):
    """swap the number in the pivot point for number to the right of the one that's greater"""
    target = nums[pivot_index]
    for num in reversed(range(pivot_index, len(nums))):
        # if the number is greater than target value:
        if nums[num] > target:
            swapper(nums, pivot_index, num)
            return

    return

def reverseRemainingSlice(nums: List[int], index: int,):
    """reverse to right of provided index"""
    for num in reversed(range(index + 1, len(nums) -1)):
        swapNUmber = nums.pop(num)
        nums.append(swapNUmber)

def swapper(nums: List[int], left: int, right: int):
    """Updates the list by swapping elements in the left and right indexes"""
    rightNumber = nums.pop(right)
    nums[left], nums[right] = nums[right], nums[left]
    return

def PermutationLexi(self, nums: List[int]):
    pivot_index = findPivot(nums)
    if pivot_index == -1:
        nums.reverse()
        return
    swapPivot(nums, pivot_index)
    reverseRemainingSlice(nums, pivot_index)

print(Permutation(1, a))

### Approach
# Identify the index of the number that breaks the increasing sequence from right to left
# find the least possible number to the right of that index that can be swapped for the target number\
# Reverse the order of the slivce of the list to the right of the number


