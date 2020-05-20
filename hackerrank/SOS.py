s = 'SOSTOT'

def callsign(s):
    exp = "SOS" * (len(s) // 3)
    return sum([tup[0] != tup[1] for tup in zip(exp, s)])

print(callsign(s))
