from collections import defaultdict


def is_isomorphic(s, t):
    mapping = {}
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        elif t[i] in mapping.values():
            return False
        else:
            mapping[s[i]] = t[i]

    return True


def is_isomorphic_amazon(words):
    result = defaultdict(list)
    for word in words:
        hash_map = {}
        y = 1
        for i in range(len(word)):
            if word[i] not in hash_map:
                hash_map[word[i]] = str(y)
                y += 1
        key = ''.join(hash_map.values())
        result[key].append(word)
    return list(result.values())


if __name__ == '__main__':
    # print(is_isomorphic('badc', 'baba'))
    # print(is_isomorphic('egg', 'add'))
    # print(is_isomorphic('foo', 'bar'))
    # print(is_isomorphic('paper', 'title'))

    print(is_isomorphic_amazon(["offer", "boo", "apple", "apply", "egg", "can"]))
