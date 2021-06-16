class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        maxRow = len(obstacleGrid) - 1
        maxCol = len(obstacleGrid[0]) - 1
        if obstacleGrid[maxRow][maxCol] == 1:
            return 0
        row = maxRow
        col = maxCol
        while row >= 0:
            col = maxCol
            while col >= 0:
                if row == maxRow and col == maxCol:
                    obstacleGrid[row][col] = 1
                else:
                    if obstacleGrid[row][col] == 0:
                        sub = 0
                        if row < maxRow:
                            sub += obstacleGrid[row + 1][col]
                        if col < maxCol:
                            sub += obstacleGrid[row][col + 1]
                        obstacleGrid[row][col] = sub
                    else:
                        obstacleGrid[row][col] = 0
                col -= 1
            
            row -= 1
        return obstacleGrid[0][0]