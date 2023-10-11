from collections import deque


def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rotten = deque()
    time = 0
    freshCount = 0
    ROWS = len(grid)
    COLUMNS = len(grid[0])

    for r in range(ROWS):
        for c in range(COLUMNS):
            if grid[r][c] == 2:
                rotten.append([r, c])
            if grid[r][c] == 1:
                freshCount += 1

    DIRECTIONS = [[0,-1], [0, 1], [-1, 0], [1, 0]]
    while rotten and freshCount > 0:

        for i in range(len(rotten)):
            r, c = rotten.popleft()

            for dr, dc in DIRECTIONS:
                row, column = r + dr, c + dc

                if (row < 0 or row == ROWS or
                    column < 0 or column == COLUMNS
                    or grid[row][column] != 1):
                    continue

                grid[row][column] = 2
                rotten.append([row, column])
                freshCount -= 1

        time += 1

    return time if freshCount == 0 else -1


# Runtime 26ms Beats 87.45%
# Memory 13.2MB Beats 53.21%
