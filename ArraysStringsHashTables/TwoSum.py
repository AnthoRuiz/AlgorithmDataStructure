# Brute Force O(N^2)
def two_sum_brute(arr, target):
    if arr is None or len(arr) < 2:
        return []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


# Optimizing using dictionary O(N)
def two_sum_dict(arr, target):
    sum_dict = {}

    if arr is None or len(arr) < 2:
        return []

    for i in range(len(arr)):
        comp = target - arr[i]
        if comp in sum_dict.keys():
            return [sum_dict.get(comp), i]
        else:
            sum_dict[arr[i]] = i
    return []


if __name__ == '__main__':
    print(two_sum_brute([9, 2, 5, 6], 7))
    print(two_sum_brute([1, 4, 10, -3], 14))
    print(two_sum_brute([9, 5, 1, 23], 10))
    print(two_sum_brute([9, 5, 1, 23], 100))

    print("========================")

    print(two_sum_dict([9, 2, 5, 6], 7))
    print(two_sum_dict([1, 4, 10, -3], 14))
    print(two_sum_dict([9, 5, 1, 23], 10))
    print(two_sum_dict([9, 5, 1, 23], 100))
    print(two_sum_dict([], 100))
    print(two_sum_dict([9], 100))
