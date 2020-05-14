from collections import deque


def sliding_window_max(nums, k):
    maxs = []
    q = deque()

    for i, n in enumerate(nums):
        # remove elements from the Queue so long as the current number is greater that the element
        while len(q) > 0 and n > q[-1]:
            q.pop()

            # add the number once all smaller numbers have been evicted from the Queue
        q.append(n)

        # calculate the window range
        window = i - k + 1
        # so long as the window's range == k, we'll add elements to the Queue
        if window >= 0:
            # add the max element, in this case the first element in the Queue, to the output List
            maxs.append(q[0])

            # check if the number on the left side of the window is going to be evicted in the next iteration
            # if it is, and if that value is at the front of the Queue, we need to evict it from the Queue
            if nums[window] == q[0]:
                q.popleft()

    return maxs


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))
