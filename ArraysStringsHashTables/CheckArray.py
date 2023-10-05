# Brute Force O(N^2)
def is_unique_brute(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                return False
    return True


# Optimizing using HashMap O(N) or O(1) because we can have more than
# 128 Characters, we are going to assume that we are working with ASCII
def is_unique_hash(s):
    hash_s = {}
    MAX_ASCII = 128

    if len(s) > MAX_ASCII:
        return False
    else:
        for i in range(len(s)):
            if s[i].lower() in hash_s.keys():
                return False
            else:
                hash_s[s[i].lower()] = s[i]

    return True


if __name__ == '__main__':
    print(is_unique_hash("ABC"))
