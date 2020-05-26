
# Convert input string to array
# numbers are regarded as integers
# s: input string
def toarray(s):
    v, a = '', []
    for c in s:
        if (c >= '0' and c <= '9') or c == '.':
            v += c
        else:
            if len(v) > 0:
                a.append(int(v));
                v = ''
            a.append(c)
    if len(v) > 0: a.append(int(v))
    return a


# Binary operation
# l: left operand
# r: right operand
# op: operator
# return: result value
def calc(l, r, op):
    if op is '+': return l + r
    if op is '-': return l - r
    if op is '*': return l * r
    if op is '/': return l / r
    return 0


# Expression evaluation
# s: string expression
# return: evaluation result
def expeval(s):
    # precedence definition
    ops = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    opr, num = [], []
    # convert input string to array
    f = toarray(s.replace(' ', ''))
    # check input
    for v in f:
        if type(v) is int:  # operand
            num.append(v)
        elif v in ['+', '-', '*', '/']:  # operator
            if len(opr) < 1 or ops[v] > ops[opr[-1]]:
                opr.append(v)
            else:
                while len(opr) > 0:
                    op = opr.pop()
                    if op in ['(', ')']: break
                    r, l = num.pop(), num.pop()
                    num.append(calc(l, r, op))
                opr.append(v)
        elif v == '(':  # open parenthes
            opr.append(v)
        elif v == ')':  # close parenthes
            while len(opr) > 0:
                op = opr.pop()
                if op is '(': break
                r, l = num.pop(), num.pop()
                num.append(calc(l, r, op))
    # remain
    while len(opr) > 0:
        op = opr.pop()
        r, l = num.pop(), num.pop()
        num.append(calc(l, r, op))

    return num[0]


# s=input()
s = '(6+5)*(4+3)+(2+1)'
print('input:', s)
print('result:', expeval(s))