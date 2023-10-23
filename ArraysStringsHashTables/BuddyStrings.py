def buddy_strings(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal and len(set(s)) < len(s):
        return True

    diff = []

    for x in range(len(s)):
        if s[x] != goal[x]:
            diff.append([s[x], goal[x]])

    if len(diff) == 2 and diff[0] == diff[-1][::-1]:
        return True

    return False


if __name__ == '__main__':
    print(buddy_strings("aa", "aa"))
