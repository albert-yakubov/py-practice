string = "AABAAB"
count = 0
for char in range(len(string) - 1): # returns 0 1 2 3 4
    print(char)
    if string[char] == string[char + 1]: # igf more than one same letter
        print(string)
        count += 1
    print(count)
# return count

