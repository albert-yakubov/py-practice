def threeNumberSum(arr, target):
    # Write your code here
    ans = {} # use the keys of the dict to store answers: prevents duplicates
    arr = sorted(arr) # sorted array allows us to make certain assumptions
    for i, a in enumerate(arr): # fix a := nums[i] in outermost iteration loop
        # j is the left pointer, k is the right pointer
        j, k = i+1, len(arr)-1
        while j < k: # while there is no overlap/collision of pointers
            # b := nums[j] is the next smallest number after a := nums[i]
            # c := nums[k] is the largest number
            b = arr[j]
            c = arr[k]
            if a+b+c == target: # found a solution
            # sort the answer so ordering doesn't matter: identifies duplicates
            # use sorted tuple as dict key to prevent duplicates
                ans[tuple(sorted((a,b,c)))] = True
                # solution is unique, move both j,k pointers
                j += 1
                k -= 1
            elif a+b+c > target: # if solution is too big,
                # move right pointer to a smaller number
                k -= 1
            elif a+b+c < target: # if solution is too small,
                # move left pointer to a bigger number
                j += 1
    return ans.keys() 
