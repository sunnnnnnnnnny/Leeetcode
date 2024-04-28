class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # go through the grid if no island seed to explore
        # once find a land, do dfs/bfs to explore it and add the loc to visited
        # time cost O(2*M*N) cause one for all grid one for dfs/bfs
        self.visited = set()
        maxX = len(grid)
        maxY = len(grid[0])
        nextDir = [[0,1], [0,-1], [1,0], [-1,0]]
        def dfs(self, x, y, grid, maxX, maxY):
            for next in nextDir:
                nextX = x+next[0]
                nextY = y+next[1]
                if nextX<0 or nextX>=maxX or nextY<0 or nextY>=maxY:
                    continue
                if (nextX, nextY) in self.visited:
                    continue
                if grid[nextX][nextY] == "1":
                    self.visited.add((nextX, nextY))
                    dfs(self, nextX, nextY, grid, maxX, maxY)
        islandCnt = 0
        for i in range(maxX):
            for j in range(maxY):
                if grid[i][j] == "1":
                    # print((i,j))
                    if (i, j) in self.visited:
                        continue
                    dfs(self, i, j, grid, maxX, maxY)
                    islandCnt+=1
        return islandCnt


        