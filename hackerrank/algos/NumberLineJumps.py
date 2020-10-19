# positive number jumps
# first starts at 1 and jumps by 1
# seconds starts at 2 and jumps by 2
# when will they meet

# so if #1 starts at 2 and jumps once it will end up on 3
# the #2 starts at 1 and jumps 2 spaces it will end up on same spot


# Complete the kangaroo function below.
# appears all those are ints
def kangaroo(x1, v1, x2, v2):
    # as long as jumps are behind
    if v1 > v2:
        remainder = (x1 - x2) % (v2 - v1)
        if remainder == 0:
            return "YES"
    return "NO"
