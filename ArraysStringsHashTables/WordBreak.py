def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]


if __name__ == '__main__':
    print(word_break('leetcode', ["leet", "code"]))
    # print(word_break('applepenapple', ["apple", "pen"]))
    # print(word_break('catsandog', ["cats", "dog", "sand", "and", "cat"]))
    # print(word_break('a', ["a"]))
    # print(word_break('a', ["b"]))
    print(word_break('apple', ["pear", "apple", "peach"]))
    print(word_break('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                     'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
                     ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
