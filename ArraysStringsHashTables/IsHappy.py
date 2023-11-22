def isHappy(n):
    visited = set()

    while n not in visited:
        visited.add(n)
        print(n)
        n = calcSquares(n)
        if n == 1:
            return True
    return False


def calcSquares(n):
    total = 0
    while n:
        digit = n % 10
        digit = digit ** 2
        total += digit
        n = n // 10
    return total


if __name__ == '__main__':
    print(isHappy(19))
