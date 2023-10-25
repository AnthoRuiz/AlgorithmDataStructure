def max_profit(prices):
    left_pointer = 0  # Buy
    right_pointer = 1  # sell
    result = 0
    while right_pointer < len(prices):
        if prices[right_pointer] - prices[left_pointer] < 0:
            left_pointer = right_pointer
            right_pointer += 1
        else:
            result = max(result, prices[right_pointer] - prices[left_pointer])
            right_pointer += 1
    return result


def max_profit_2(prices):
    l, r = 0, 1
    result = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            result = max(result, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return result


if __name__ == '__main__':
    print(max_profit([7, 6, 4, 3, 15]))
    print(max_profit_2([7, 6, 4, 3, 15]))
