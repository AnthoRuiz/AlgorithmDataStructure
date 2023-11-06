def generate(numRows):
    triangle = [[1]]
    for i in range(numRows - 1):
        tmp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        triangle.append(row)
    return triangle


if __name__ == '__main__':
    print(generate(5))
