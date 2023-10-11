# you can define helper methods if needed
def is_palindrome(s):
    index_l = 0
    index_r = len(s) - 1

    while index_l < index_r:
        if s[index_r] != s[index_l]:
            return False
        index_l += 1
        index_r -= 1
    return True


def palindrome_python(s):
    if s == s[::-1]:
        return True
    return False


# TIME COMPLEXITY: O(n) because we iterate through the list one time from the start and the end at the same time
# using two pointers

# SPACE COMPLEXITY: O(n) because we are creating a new string
def valid_palindrome(s):
    tmp_s = s.lower().replace(" ", "")
    tmp_s = ''.join(filter(str.isalnum, tmp_s))
    return is_palindrome(tmp_s)


# TIME COMPLEXITY: O(n) because we iterate through the list one time from the start and the end at the same time
# using two pointers

# SPACE COMPLEXITY: O(1) because we are not creating a new string
def valid_palindrome_2(s):
    index_l = 0
    index_r = len(s) - 1
    while index_l != index_r and not (index_l > index_r):
        if s[index_l].isalpha() or s[index_l].isnumeric():
            if s[index_r].isalpha() or s[index_r].isnumeric():
                if s[index_l].lower() != s[index_r].lower():
                    return False
                index_l += 1
                index_r -= 1
            else:
                index_r -= 1
        else:
            index_l += 1
    return True


if __name__ == '__main__':
    print(valid_palindrome_2('race a car'))
