from collections import defaultdict


def get_anagram_hash(s):
    letter_count = [0] * 26
    for i in range(len(s)):
        letter_count[ord(s[i]) - ord('a')] += 1
    return letter_count


def build_hash_map(arr_words):
    res = defaultdict(list)
    for s in arr_words:
        word_hash = get_anagram_hash(s)
        res[tuple(word_hash)].append(s)
    return res.values()


def group_anagrams(words):
    if words is None or len(words) == 0:
        return []
    return list(build_hash_map(words))


def group_anagrams_2(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams_2(['saco', 'arresto', 'programa', 'rastreo', 'caso']))
