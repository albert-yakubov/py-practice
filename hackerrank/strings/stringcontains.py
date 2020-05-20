s2 = 'hereiamstackerrank'
def hr(s):
    count = 0
    for char in 'hackerrank':
        if char in s[count:]:
            count = s.index(char, count) + 1
        else:
            return 'NO'
    return 'YES'


print(hr(s2))