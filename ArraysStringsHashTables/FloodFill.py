def floodFill(image, sr, sc, color):
    visit = set()
    starting = image[sr][sc]

    def dfs(i, j, starting):
        if i >= len(image) or j >= len(image[0]) or i < 0 or j < 0 or image[i][j] != starting:
            return

        if (i, j) in visit:
            return

        image[i][j] = color
        visit.add((i, j))

        dfs(i - 1, j, starting)
        dfs(i + 1, j, starting)
        dfs(i, j - 1, starting)
        dfs(i, j + 1, starting)

    dfs(sr, sc, starting)
    return image


if __name__ == '__main__':
    print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
