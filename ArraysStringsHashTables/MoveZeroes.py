def move_zeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    return nums


if __name__ == '__main__':
    print(move_zeroes([0, 1, 0, 3, 12]))
    print(move_zeroes([1, 2]))
