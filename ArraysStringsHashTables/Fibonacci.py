def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_memo(n):
    fib_cache = {0: 0, 1: 1}

    for i in range(2, n + 1):
        fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2]

    return fib_cache[n]


def fib_dp(n):
    if n <= 1:
        return n
    fib_array = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
    return fib_array[n]


def tribonacci(n):
    fib_array = [0, 1, 1] + [0] * (n - 1)
    for i in range(3, n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2] + + fib_array[i - 3]
    return fib_array[n]


if __name__ == '__main__':
    print(tribonacci(25))
