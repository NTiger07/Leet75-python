from collections import deque
maze1 = [["+", "+", ".", "+"], [".", ".", ".", "+"],
         ["+", "+", "+", "."]]  # . means empty cells
# Output 1                                      + means walls
entrance1 = [1, 2]


def nearestExit(maze, entrance):
    ROWS, COLUMNS = len(maze), len(maze[0])
    # Entrance and number of steps
    queue = deque([(entrance[0], entrance[1], 0)])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # Up, down, left, right
    visited = set()
    visited.add((entrance[0], entrance[1]))

    # Now BFS
    while queue:
        x, y, steps = queue.popleft()

        if (x, y) != (entrance[0], entrance[1]) and (x == 0 or x == ROWS - 1 or y == 0 or y == COLUMNS - 1) and (maze[x][y] == "."):
            return steps

        for dx, dy in directions:
            xx, yy = x + dx, y + dy
            if 0 <= xx < ROWS and 0 <= yy < COLUMNS and maze[xx][yy] == "." and (xx, yy) not in visited: # This block of code checks if the next position (new_x, new_y) is within the 
                queue.append((xx, yy, steps + 1))                                                        # boundaries of the maze (0 <= new_x < rows and 0 <= new_y < cols), is not a wall (indicated by maze[new_x][new_y] == '.'), 
                visited.add((xx, yy))                                                                    # and has not been visited before (indicated by (new_x, new_y) not in visited). If all these conditions are met, 
                                                                                                         # the code appends the next position to the queue for further exploration and adds it to the visited set to avoid revisiting the same position.


    return -1


print(nearestExit(maze1, entrance1))
