def rob(houses):
    rob1, rob2 = 0, 0
    for h in houses:
        tmp = max(h + rob1, rob2)
        rob1 = rob2
        rob2 = tmp
    return rob2


if __name__ == '__main__':
    print(rob([2, 7, 9, 3, 1]))
