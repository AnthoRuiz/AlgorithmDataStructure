def roman_integer(s):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and symbols[s[i]] < symbols[s[i + 1]]:
            total -= symbols[s[i]]
        else:
            total += symbols[s[i]]

    return total


def int_roman(num):
    sym_list = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
    total = ""
    for sym, val in reversed(sym_list):
        if num // val:
            count = num // val
            total += (sym * count)
            num = num % val

    return total


if __name__ == '__main__':
    # print(roman_integer('MCMXCIV'))
    # print(roman_integer('IX'))
    print(int_roman(9))
