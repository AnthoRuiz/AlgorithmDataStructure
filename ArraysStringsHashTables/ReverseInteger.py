def reverse_integer(n):
    reversed_int = 0
    while n > 0:
        remainder = n % 10
        reversed_int = reversed_int * 10 + remainder
        n = n // 10
    return reversed_int


if __name__ == '__main__':
    print(reverse_integer(358))
