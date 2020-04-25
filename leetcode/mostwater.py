class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = 0
        j = len(height) - 1
        while i<j:
            max_area = max(max_area, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
if __name__ == "__main__":
    x =[1,8,6,2,5,4,8,3,7]
    max_area = Solution.maxArea(x, [8, 7])
    print(max_area)



