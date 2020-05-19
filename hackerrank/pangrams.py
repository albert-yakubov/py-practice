import string
def pangrams(s):
    alpha = []
    beta = []
    beta.sort()

    for letter in string.ascii_lowercase:
        alpha.append(letter)


    for ltr in s:
        if ltr != " ":
            beta.append(ltr.lower().replace(" ", ""))
            beta.sort()
            beta = list(dict.fromkeys(beta))
    if beta == alpha:
        return 'pangram'

    else:
        return 'not pangram'


s= 'We promptly judged antique ivory buckles for the next prize'
print(pangrams(s))