def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    result = ['']
    if digits == '': return []
    digit_mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    for digit in digits:
        result = [x + var for x in result for var in digit_mapping[digit]]
    return result