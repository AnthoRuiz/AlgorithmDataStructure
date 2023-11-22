def removeDuplicates(nums):
    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left


if __name__ == '__main__':
    print(removeDuplicates([1, 2, 3]))
    print(removeDuplicates([1, 1, 2]))
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
