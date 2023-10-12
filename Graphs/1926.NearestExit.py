from collections import deque


maze1 = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]] # . means empty cells
entrance1 = [1,2] # Output 1                                      + means walls

def nearestExit(maze, entrance):
    ROWS, COLUMNS = len(maze), len(maze[0])
    
    #Check if cell is at the border of the grid
    
    def isExit(r, c):
        isEntrance = r == entrance[0] and c == entrance[1] # Returns true if cell is the starting point
        isEdge = r == 0 or c == 0 or r == ROWS - 1 or c == COLUMNS - 1 # Returns true if cell is at the border
        return not isEntrance and isEdge
    
    #Now BFS


print(nearestExit(maze1,entrance1))