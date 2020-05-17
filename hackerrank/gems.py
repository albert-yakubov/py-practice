
# find the string of minimum len
# find the number of chars in that string
# that are present in that string
def gemstones(arr):
    min_len = min(list(map(len, arr)))
    print(min_len)
    gem = 0
    for a in arr:
        if len(a) == min_len:
            min_word = a
            break
    print(min_word)
    for a in min_word:
        count = 1
        for b in range(len(arr)):
            new_list = list(arr[b])
            if a not in new_list:
                count = 0
                break
            else:
                del new_list[new_list.index(a)]
                arr[b] = "".join(new_list)
        if count == 1:
            gem += 1
    return gem

arr = ['abcdde', 'baccd', 'eeabg']
print(gemstones(arr))