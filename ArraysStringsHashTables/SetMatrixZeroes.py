# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

def set_zeroes(m):
    first_row = False
    ROWS, COLS = len(m), len(m[0])

    # Checking what Row need to be 0
    for r in range(ROWS):
        for c in range(COLS):
            if m[r][c] == 0:
                m[0][c] = 0
                if r > 0:
                    m[r][0] = 0
                else:
                    # update our first Row to True in case the first row == 0
                    first_row = True

    # Set 0 in the "internal" matrix without the first col and row
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if m[0][c] == 0 or m[r][0] == 0:
                m[r][c] = 0

    if m[0][0] == 0:
        for r in range(ROWS):
            m[r][0] = 0

    if first_row:
        for c in range(COLS):
            m[0][c] = 0


if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(matrix)
    print(set_zeroes(matrix))
