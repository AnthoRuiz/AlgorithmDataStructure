def majority_element(nums):
    hash_map = {}
    res, maxCount = 0, 0
    for i in range(len(nums)):
        if nums[i] in hash_map:
            hash_map[nums[i]] += 1
        else:
            hash_map[nums[i]] = 1

        if hash_map[nums[i]] > maxCount:
            res = nums[i]
        else:
            res = res
        maxCount = max(maxCount, hash_map[nums[i]])
    return res


def majority_element_op(nums):
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if res == n else -1)
    return res


if __name__ == '__main__':
    print(majority_element_op([2, 2, 1, 1, 1, 2, 2]))
