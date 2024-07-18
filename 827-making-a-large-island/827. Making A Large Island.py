class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # identify all island and it's size
        # check all water that can link any 2 islands, the max is by adding the size
        # time: O(n*M) space:O(N*M)
        island2Size = {}
        def explorIsland(x, y, m, n, islandIdx):
            exploreSize = 1
            if x-1>=0 and grid[x-1][y] == 1:
                grid[x-1][y] = islandIdx
                exploreSize += explorIsland(x-1,y, m,n, islandIdx)
            if x+1<m and grid[x+1][y] == 1:
                grid[x+1][y] = islandIdx
                exploreSize += explorIsland(x+1,y, m,n, islandIdx)
            if y-1>=0 and grid[x][y-1] == 1:
                grid[x][y-1] = islandIdx
                exploreSize += explorIsland(x,y-1, m,n, islandIdx)
            if y+1<n and grid[x][y+1] == 1:
                grid[x][y+1] = islandIdx
                exploreSize += explorIsland(x,y+1, m,n, islandIdx)
            return exploreSize
        m = len(grid)
        n = len(grid[0])
        nowIslandIdx = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = nowIslandIdx
                    islandSize = explorIsland(i,j,m,n,nowIslandIdx)
                    island2Size[nowIslandIdx] = islandSize
                    nowIslandIdx += 1
        # print(island2Size)
        if len(island2Size.keys()) == 1:
            # if there's water size should add one
            oneIslandSize = island2Size[nowIslandIdx-1]
            return oneIslandSize+1 if oneIslandSize<(n*m) else oneIslandSize
        elif len(island2Size.keys()) == 0:
            return 1
        
        maxIslandSize = max(island2Size.values())
        # print(maxIslandSize)
        def checkConnectSize(nearIsland):
            realIsland = set()
            connectSize = 1
            for idx in nearIsland:
                if idx>0:
                    if idx not in realIsland:
                        connectSize += island2Size[idx]
                    realIsland.add(idx)
            return connectSize
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    up = grid[i-1][j] if i-1>=0 else -1
                    down = grid[i+1][j] if i+1<m else -1
                    left = grid[i][j-1] if j-1>=0 else -1
                    right = grid[i][j+1] if j+1<n else -1
                    nowSize = checkConnectSize([up, down, left, right])
                    maxIslandSize = max(maxIslandSize, nowSize)
        return maxIslandSize


        