# Time complexity:
# O(n) -> As we are traversing the vector 1 time.
#
# Space complexity:
# O(1)

def climbing_stairs(n):

    if n == 0 or n == 1:
        return 1

    one, two = 1, 1

    for i in range(n - 1):
        tmp = one
        one = one + two
        two = tmp

    return one


if __name__ == '__main__':
    print(climbing_stairs(5))
