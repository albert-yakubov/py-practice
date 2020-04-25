
class Solution:
    nums = [1, 2, 3]
    target = 4
    def combinationSum4(self, nums, target):
        dictionary = dict()
        def depth_first_searh(target):
            ways = 0
            if target in dictionary:
                return dictionary[target]
            if target == 0:
                return 1
            for num in nums:
                if target >= num:
                    ways += depth_first_searh(target - num)
            dictionary[target]= ways

            return ways
        
        print(depth_first_searh(target))
        return depth_first_searh(target)

if __name__ == "__main__":
    nums = [1, 2, 3]
    target = Solution().combinationSum4(nums, 4)

    print(target)
    


