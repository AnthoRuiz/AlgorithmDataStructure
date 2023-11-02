def min_cost_climbing_stairs(costs):
    costs.append(0)
    for i in range(len(costs) - 3, -1, -1):
        costs[i] += min(costs[i + 1], costs[i + 2])

    return min(costs[0], costs[1])


if __name__ == '__main__':
    print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
