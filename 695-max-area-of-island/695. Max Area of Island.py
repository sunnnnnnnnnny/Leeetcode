class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # use bfs or dfs for searching the new land of the whole island 
        # keep track of the maxArea of all islands
        # time: O(N*M*2) space:O(1) if we can modify grid inspace
        N = len(grid)
        M = len(grid[0])
        maxArea = 0
        def bfs(nowX, nowY):
            nonlocal N, M, grid
            if grid[nowX][nowY] != 1:
                return 0
            grid[nowX][nowY] = 2
            addArea = 1
            if nowX-1>=0:
                addArea+= bfs(nowX-1, nowY)
            if nowX+1<N:
                addArea+= bfs(nowX+1, nowY)
            if nowY-1>=0:
                addArea+= bfs(nowX, nowY-1)
            if nowY+1<M:
                addArea+= bfs(nowX, nowY+1)
            return addArea
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    curArea = bfs(i,j)
                    maxArea = max(maxArea, curArea)
        return maxArea

