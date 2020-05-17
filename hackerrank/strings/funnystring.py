fs = "12345"

def funny(s):
    my_list = []
    reversed_list = []
    reveresed_string = s[::-1]

    for char in range(len(s) -1):
        new_char = char + 1
        my_list.append(abs((ord(s[new_char])-ord(s[char]))))
        reversed_list.append(abs((ord(reveresed_string[new_char]) - ord(reveresed_string[char]))))

    for char in range(len(my_list)):
        if (my_list[char] - reversed_list[char]) != 0:
            return "Not Funny"
        if char == len(my_list) - 1:
            return "Funny"


print(funny(fs))
