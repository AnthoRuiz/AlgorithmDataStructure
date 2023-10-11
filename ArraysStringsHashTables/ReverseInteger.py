import math


def reverse_integer(n):
    reversed_int = 0
    while n > 0:
        remainder = n % 10
        reversed_int = reversed_int * 10 + remainder
        n = n // 10
    return reversed_int


def reverse_integer_2(x) -> int:
    MAX_INT = 2 ** 31 - 1  # 2,147,483,647
    MIN_INT = -2 ** 31  # -2,147,483,648
    result = 0

    while x != 0:
        if result > MAX_INT / 10 or result < MIN_INT / 10:
            return 0
        digit = x % 10 if x > 0 else x % -10
        result = result * 10 + digit
        x = math.trunc(x / 10)

    return result


if __name__ == '__main__':
    print(reverse_integer_2(1534236469))
    print(reverse_integer_2(-123))
