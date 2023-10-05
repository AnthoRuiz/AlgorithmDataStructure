# Brute Force
def is_unique_brute(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                return False
    return True


# Optimizing using HashMap
def is_unique_hash(s):
    hash_s = {}
    for i in range(len(s)):
        if s[i].lower() in hash_s.keys():
            return False
        else:
            hash_s[s[i].lower()] = s[i]
    return True


if __name__ == '__main__':
    print(is_unique_hash("bbbB"))
