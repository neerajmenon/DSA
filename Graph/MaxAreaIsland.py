class Solution:
    def maxAreaOfIsland(self,grid):

        if not grid or not grid[0]:
            return 0

        maxArea = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r, c) in visit:
                return 0

            visit.add((r, c))
            area = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs(r, c)
                    maxArea = max(area,maxArea)
        return maxArea

