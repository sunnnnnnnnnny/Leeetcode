class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # check the grid how many edge with the waterr
        def howManyEdgeWater(self, x:int, y:int, grid: List[List[int]]):
            edgeCnt = 0
            # up
            if y==0 or grid[x][y-1] == 0:
                edgeCnt +=1
            # down
            if y==len(grid[x])-1 or grid[x][y+1] == 0:
                edgeCnt +=1
            if x==0 or grid[x-1][y] == 0:
                edgeCnt +=1
            if x==len(grid)-1 or grid[x+1][y] == 0:
                edgeCnt +=1
            return edgeCnt
        def betterCntOfTwoEdge(self, x:int, y:int, grid: List[List[int]]):
            edgeCnt = 4
            # up is land
            if not (y==0 or grid[x][y-1] == 0):
                edgeCnt -=2
            # left
            if not(x==0 or grid[x-1][y] == 0):
                edgeCnt -=2
            return edgeCnt
        ret = 0
        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[i]), 1):
                if grid[i][j]:
                    ret += betterCntOfTwoEdge(self, i, j, grid)
                    # ret += howManyEdgeWater(self, i, j, grid)
        return ret

            

        