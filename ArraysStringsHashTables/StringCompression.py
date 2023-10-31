def string_compression(s):
    result = ''
    counter = 1
    i = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            counter += 1
        else:
            result += s[i] + str(counter)
            counter = 1
    result += s[i] + str(counter)
    return result


def compress(chars):
    nu_chars = len(chars)

    if nu_chars < 2:
        return nu_chars

    i = j = 0
    while i < nu_chars:
        count = 1
        while i < len(chars) - 1 and chars[i] == chars[i + 1]:
            count += 1
            i += 1
        chars[j] = chars[i]
        j += 1
        if count > 1:
            for val in str(count):
                chars[j] = val
                j += 1
        i += 1

    return j


if __name__ == '__main__':
    print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
    print(string_compression(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
