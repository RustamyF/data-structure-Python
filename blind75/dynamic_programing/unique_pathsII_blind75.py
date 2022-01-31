"""Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # if the starting point is blocked, we cannot move
        if obstacleGrid[0][0] == 1:
            return 0
        # set the first grid equal to one
        obstacleGrid[0][0]=1
    # change the first column to one
        row=len(obstacleGrid)
        for i in range(1,row):
            # if before is one and after is zeros, we set it to one. Otherwise, it is zero
            if obstacleGrid[i-1][0]==1 and obstacleGrid[i][0]==0:
                obstacleGrid[i][0]=1
            else:
                obstacleGrid[i][0]=0

        # change the first row
        col=len(obstacleGrid[0])
        for i in range(1,col):
            # if before is one and after is zeros, we set it to one. Otherwise, it is zero
            if obstacleGrid[0][i-1]==1 and obstacleGrid[0][i]==0:
                obstacleGrid[0][i]=1
            else:
                obstacleGrid[0][i] = 0
        # now go over each row and column
        for r in range(1, row):
            for c in range(1,col):
                # if there is obstacle, put the value az zero
                if obstacleGrid[r][c]==1:
                    obstacleGrid[r][c]=0
                # if there is not obstacle, add the cell above and and to the left of current cell
                else:
                    obstacleGrid[r][c]=obstacleGrid[r-1][c]+obstacleGrid[r][c-1]
        # return the last cell
        return obstacleGrid[-1][-1]




obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
my_result=Solution()
print(my_result.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,1],[0,0]]
my_result=Solution()

print(my_result.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid=[[0,0],[1,1],[0,0]]
print(my_result.uniquePathsWithObstacles(obstacleGrid))