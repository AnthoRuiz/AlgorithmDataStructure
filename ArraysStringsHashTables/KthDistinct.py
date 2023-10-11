def kthDistinct(arr, k):
    dict_ocurr = {}

    for c in arr:
        if c in dict_ocurr.keys():
            tmp = dict_ocurr[c]
            tmp += 1
            dict_ocurr[c] = tmp
        else:
            dict_ocurr[c] = 1

    con = 0
    result = ""
    for item in dict_ocurr:
        if dict_ocurr[item] == 1:
            con += 1
            if con == k:
                result = item

    if con < k:
        return ""
    else:
        return result


if __name__ == '__main__':
    print(kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
