# Brute Force O(N^2)
def getConcatenation_brute(nums):
    times = 0
    res = []
    while times < 2:
        for n in nums:
            res.append(n)
        times += 1
    return res


# O(N) using Space O(N)
def getConcatenation_space(nums):
    res = [None] * (2 * len(nums))
    size = len(nums)
    for i in range(len(nums)):
        res[i] = nums[i]
        res[size + i] = nums[i]
    return res


# O(N), Space O(1)
def getConcatenation(nums):
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums


if __name__ == '__main__':
    print(getConcatenation([1, 2, 1]))
    print(getConcatenation([1, 3, 2, 1]))
