class Solution(object):
    def search(self, nums, target):
        
        return self.bfs(nums,target,0,len(nums)-1)

        # trying to us reccursion on the solution:
        # we will need the numbers, the high and the low and the target
    def bfs(self, nums, target, low, high):
            
            
        # find the medium of the array
        med = int(low + (high- low)/ 2)
        # then divide it down the middle
        new_size = high - low + 1
            
        # if noting found return -1
        if new_size <= 0:
            return -1
        # if the number is in the lower half return low:
        elif nums[low]==target:
            return low
        # if in higher return higher
        elif nums[med]== target:
            return med
        elif nums[high]==target:
            return high            
        # if out of index return not found
        elif new_size <=3:
            return -1
            
        else:
            num_lo=nums[low]
            num_hi=nums[high]
            num_md=nums[med]

            if num_lo < num_md:
                #left subarray is sorted
                if num_lo < target < num_md:
                    #target is on left side
                    return self.bfs(nums,target,low+1,med-1)
                else:
                    #target is on right side
                    return self.bfs(nums,target,med+1,high-1)
            else:
                #right subarray is sorted
                if num_md < target < num_hi:
                    #target is on right side
                    return self.bfs(nums,target,med+1,high-1)
                else:
                    #target is on left side
                    return self.bfs(nums,target,low+1,med-1)