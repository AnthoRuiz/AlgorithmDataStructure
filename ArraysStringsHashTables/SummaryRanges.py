def summary_ranges(nums):
    result = []
    i = 0

    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[j - 1] + 1 == nums[j]:
                j += 1
            else:
                break
        if j - i == 1:
            result.append(str(nums[j - 1]))
        else:
            result.append(str(nums[i]) + "->" + str(nums[j - 1]))
        i = j
    return result


if __name__ == '__main__':
    print(summary_ranges([0, 1, 2, 4, 5, 7]))
