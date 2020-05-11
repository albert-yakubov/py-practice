import re


def beautifulBinaryString(b):
    return len(re.findall('010',b))