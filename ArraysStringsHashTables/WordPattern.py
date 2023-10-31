def word_pattern(pattern, s):
    s = s.split(' ')
    mapping = {}
    if len(pattern) != len(s):
        return False

    for i in range(len(pattern)):
        if pattern[i] in mapping:
            if mapping[pattern[i]] != s[i]:
                return False
        elif s[i] in mapping.values():
            return False
        else:
            mapping[pattern[i]] = s[i]
    return True


if __name__ == '__main__':
    print(word_pattern("abba", "dog cat cat dog"))
    print(word_pattern("abba", "dog cat cat fish"))
    print(word_pattern("aaaa", "dog cat cat dog"))
