# Given an A array of integers - Reverse this A array in O(n) and Constant memory

def reverse(arr):

    # pointing to the first item
    index_r = 0
    # pointing to the last item
    index_l = len(arr) - 1

    while index_r < index_l:
        arr[index_r], arr[index_l] = arr[index_l], arr[index_r]
        index_r += 1
        index_l -= 1
    return arr


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(a)
    print(reverse(a))
