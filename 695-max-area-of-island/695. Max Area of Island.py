class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # traverse the whole grid, cound the area of island by dfs/bfs
        # keep record of it
        # time:O(2N)=O(N)
        # space:O(N)
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # bfs
                    nextGrid = [(i,j)]
                    grid[i][j] = 2
                    curArea = 0
                    while nextGrid:
                        levelLen = len(nextGrid)
                        for l in range(levelLen):
                            now = nextGrid.pop(0)
                            curArea += 1
                            x,y = now[0], now[1]
                            if x-1>=0 and grid[x-1][y] == 1:
                                grid[x-1][y] = 2
                                nextGrid.append((x-1,y))
                            if x+1<m and grid[x+1][y] == 1:
                                grid[x+1][y] = 2
                                nextGrid.append((x+1,y))
                            if y-1>=0 and grid[x][y-1] == 1:
                                grid[x][y-1] = 2
                                nextGrid.append((x,y-1))
                            if y+1<n and grid[x][y+1] == 1:
                                grid[x][y+1] = 2
                                nextGrid.append((x,y+1))
                    maxArea = max(maxArea, curArea)
        return maxArea
        