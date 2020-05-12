def quadratic(self, val, a, b, c):
    return (a*(val**2)) + (b*val) + c


def sort_transformed_array(self, nums, a, b, c):
    for i in range(len(nums)):
        nums[i] = quadratic(nums[i], a, b, c)
    nums.sort()
    return nums

def transform(self, nums, a, b, c):
    returne = []
    left = 0
    right = len(nums) -1
    middle = (left + right) //2

    while left <= right:
        quad_left = quadratic(nums[left], a, b, c)
        quad_right = quadratic(nums[right], a, b, c)
        if quad_left < quad_right:
            returne.append(quad_left)
            left += 1
        else:
            returne.append(quad_right)
            right -= 1

    return returne

nums = [-4, 2,2 ,4]
a = 1
b =1
c =1
print(transform(0, nums, a, b, c))