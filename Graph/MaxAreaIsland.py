class Solution:
    def maxAreaOfIsland(self,grid):
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0  # Mark the cell as visited

            area = 1
            area += dfs(i+1, j)  # Check the cell to the south
            area += dfs(i-1, j)  # Check the cell to the north
            area += dfs(i, j+1)  # Check the cell to the east
            area += dfs(i, j-1)  # Check the cell to the west

            return area

        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea