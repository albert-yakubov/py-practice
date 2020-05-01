def balancedBrackets(string):
    # Write your code here
    # creaste a stack:
    stack = []
    # set opening and closing brackets:
    opens_closes = {")": "(", "}": "{", "]": "[", "|": "|"}
    openers = set(opens_closes.values())
    # now enumerate through the string and check for openers and closers:
    for c in string:
        if c in openers: 
            stack.append(c)
        elif c in opens_closes:
            #if there are no opening characters return false
            if stack == []:

                return False 
            # if we got the match:
            if stack[-1] == opens_closes.get(c):
                
                stack.pop()
                return True
            else: 
                return False
    return True
        