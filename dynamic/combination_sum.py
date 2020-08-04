
class Solution:
    # nums = [1, 2, 3]
    # target = 4

    def findPairs(mylist, K):
        res = []
        while mylist:
            num = mylist.pop()
            diff = K - num
            if diff in mylist:
                res.append((diff, num))

        res.reverse()
        return res
    def combinationSum4(self, nums, target):
        dictionary = dict()
        unique = {}
        def depth_first_searh(target):
            ways = 0
            if target in dictionary:
                return dictionary[target]
            if target == 0:
                return 1
            for num in nums:
                if target >= num:
                    ways += depth_first_searh(target - num)
            dictionary[target] = ways
            #print(dictionary)
            return ways
        # print(dictionary)
        # print(depth_first_searh(target))
        return depth_first_searh(target)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    target = Solution().combinationSum4(nums, 4)

    #print(Solution.combinationSum4(0, nums, 5))
    print(Solution.findPairs(nums, 9))



