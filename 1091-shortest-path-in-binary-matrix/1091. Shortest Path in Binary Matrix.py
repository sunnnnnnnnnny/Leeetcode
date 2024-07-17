class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # backtracking with memo the shorest path to each 0 node
        # bfs by modifying the grid val to 2 as seen
        # time:O(n*n) space:O(N*N) for queue
        rootPathLen = 1
        bfs = []
        yLen = len(grid)
        xLen = len(grid[0])
        if grid[0][0] == 0:
            grid[0][0] = 2
            bfs.append((0,0))
        while bfs:
            levelCnt = len(bfs)
            for _ in range(levelCnt):
                y,x = bfs.pop(0)
                if y == x and y == yLen-1:
                    return rootPathLen
                # 8 dirction of child
                if x-1>=0 and y-1>=0 and grid[y-1][x-1] == 0:
                    grid[y-1][x-1] = 2
                    bfs.append((y-1,x-1))
                if y-1>=0 and grid[y-1][x] == 0:
                    grid[y-1][x] = 2
                    bfs.append((y-1,x))
                if y-1>=0 and x+1<xLen and grid[y-1][x+1] == 0:
                    grid[y-1][x+1] = 2
                    bfs.append((y-1,x+1))
                if x-1>=0 and grid[y][x-1] == 0:
                    grid[y][x-1] = 2
                    bfs.append((y,x-1))
                if x+1<xLen and grid[y][x+1] == 0:
                    grid[y][x+1] = 2
                    bfs.append((y,x+1))
                if x-1>=0 and y+1<yLen and grid[y+1][x-1] == 0:
                    grid[y+1][x-1] = 2
                    bfs.append((y+1,x-1))
                if y+1<yLen and grid[y+1][x] == 0:
                    grid[y+1][x] = 2
                    bfs.append((y+1,x))
                if y+1<yLen and x+1<xLen and grid[y+1][x+1] == 0:
                    grid[y+1][x+1] = 2
                    bfs.append((y+1,x+1))
            rootPathLen += 1
        return -1



        