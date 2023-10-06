
# To implement an algorithm to determine if a string contains all unique characters. .
# Input : s = “abcd”
# Output: True
# “abcd” doesn’t contain any duplicates. Hence the output is True.
#
# Input : s = “abbd”
# Output: False
# “abbd” contains duplicates. Hence the output is False.


# Brute Force O(N^2)
def is_unique_brute(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


# Optimizing using HashMap O(N) or O(1) because we can have more than
# 128 Characters, we are going to assume that we are working with ASCII
def is_unique_set(s):
    set_s = set()
    MAX_ASCII = 128

    if len(s) > MAX_ASCII:
        return False
    else:
        for i in range(len(s)):
            if s[i] in set_s:
                return False
            else:
                set_s.add(s[i])

    return True


if __name__ == '__main__':
    print(is_unique_set("dHOLAa"))
