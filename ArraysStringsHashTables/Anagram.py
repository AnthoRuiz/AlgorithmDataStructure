def is_anagram(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t


if __name__ == '__main__':
    print(is_anagram('anagram', 'nagaram'))
    print(is_anagram(' ', ' '))
