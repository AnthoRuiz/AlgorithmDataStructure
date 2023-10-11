# Approach 2 (Convert list -> Number :: -> Addition +1 :: -> Number -> List
def plus_one(digits):
    numbers = 0
    result = []
    for i in range(len(digits)):
        numbers = numbers * 10 + digits[i]

    numbers += 1

    while numbers != 0:
        result.insert(0, numbers % 10)
        numbers = numbers // 10

    return result


# Approach using Array
def plus_one_2(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits


if __name__ == '__main__':
    print(plus_one_2([1, 9]))
