
def decodeString(self, s):

    # using stack:
    stack = []
        
    for symbol in s:
        if symbol != ']':
            # append everything to newly created stack
            stack.append(symbol)
            # continue because the other [ is not taken out
            continue
        # make a new string and pop the rest of the [ << out of stack:
        new_string = ''
        while stack and stack[-1] != '[':
            new_string = stack.pop() + new_string
        stack.pop()
        # now we have to pop the numbers out:
        num = ''
        while stack and stack[-1].isnumeric():
            num = stack.pop() + num
            # then append the new values times the number that was just popped
            # so instead of 3a it will be aaa
        stack.append(int(num)*new_string)
        
        # finally return the stack removing the coma:
    return ''.join(stack)

s = '3[a]2[cb]'
print(decodeString(0, s))