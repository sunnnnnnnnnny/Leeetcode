class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # bfs from your location
        # time:O(N*M) space:O(N*M)
        loc = []
        n = len(grid)
        m = len(grid[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    loc.append((i,j))
                    visited.add((i,j))
                    break
        level = 0
        while loc:
            levelSize = len(loc)
            for i in range(levelSize):
                nowI, nowJ = loc.pop(0)
                if grid[nowI][nowJ] == '#':
                    return level
                if nowI-1>=0 and grid[nowI-1][nowJ] != 'X' and (nowI-1,nowJ) not in visited:
                    visited.add((nowI-1,nowJ))
                    loc.append((nowI-1,nowJ))
                if nowI+1<n and grid[nowI+1][nowJ] != 'X' and (nowI+1,nowJ) not in visited:
                    visited.add((nowI+1,nowJ))
                    loc.append((nowI+1,nowJ))
                if nowJ-1>=0 and grid[nowI][nowJ-1] != 'X' and (nowI,nowJ-1) not in visited:
                    visited.add((nowI,nowJ-1))
                    loc.append((nowI,nowJ-1))
                if nowJ+1<m and grid[nowI][nowJ+1] != 'X' and (nowI,nowJ+1) not in visited:
                    visited.add((nowI,nowJ+1))
                    loc.append((nowI,nowJ+1))
            level+=1
        return -1