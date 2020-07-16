# turn int to roman

# you can turn the int to string
# then use the position of the number to store exponents

the_roman_map = {
    0: {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX'
    },
    1: {
        0: '',
        1: 'X',
        2: 'XX',
        3: 'XXX',
        4: 'XL',
        5: 'L',
        6: 'LX',
        7: 'LXX',
        8: 'LXXX',
        9: 'XC'
    },

    2: {
        0: '',
        1: 'C',
        2: 'CC',
        3: 'CCC',
        4: 'CD',
        5: 'D',
        6: 'DM',
        7: 'DMM',
        8: 'DMMM',
        9: ''

    }
}


def intToRoman(self, num: int) -> str:
    num_str = str(num)
    # enumerate(prints the index and the value of the array)
    # 3712 = 3000 + 700 + 10 + 2 = 3*10^3 + 2*10^2 + 1*10^1 + 2*10^0
    len_num = len(num_str) - 1
    exponents = [(len_num - exp, int(num_val)) for exp, num_val in enumerate(num_str)]
    rom_list = [the_roman_map[exp][number] for (exp, number) in exponents]
    return ''.join(rom_list)
print(intToRoman(0, 3))

