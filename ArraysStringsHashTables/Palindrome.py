# you can define helper methods if needed
def is_palindrome(s):
    index_r = 0
    index_l = len(s) - 1

    while index_r < index_l:
        if s[index_l] != s[index_r]:
            return False
        index_r += 1
        index_l -= 1
    return True


def palindrome_python(s):
    if s == s[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome('aaaa'))
