def single_number(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res


if __name__ == '__main__':
    print(single_number([2, 2, 3, 2]))
