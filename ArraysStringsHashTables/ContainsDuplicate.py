def contains_duplicate(nums):
    hash_map = {}

    for n in nums:
        if n in hash_map:
            return True
        else:
            hash_map[n] = 1
    return False


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))
