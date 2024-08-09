class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # only need to pre-calculate the sum of each row/col = >O(r*n)
        # by going from the center of the 3*3 grid, to verify if is magic
        # time: O(r*c*2*9) = O(r*c)
        # space:O(r*c*2)
        rows = len(grid)
        cols = len(grid[0])
        gridSumX = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        gridSumY = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for x in range(rows):
            for y in range(cols):
                gridSumX[x][y+1]=gridSumX[x][y]+grid[x][y]
                gridSumY[x+1][y]=gridSumY[x][y]+grid[x][y]
        def checkBothDiagonal(expectSum, x, y):
            nonlocal grid
            leftDSum = grid[x-1][y-1]+grid[x][y]+grid[x+1][y+1]
            rightDSum = grid[x-1][y+1]+grid[x][y]+grid[x+1][y-1]
            return leftDSum==rightDSum and rightDSum==expectSum
        def getVerticalSumCheck(x, y):
            nonlocal gridSumX
            up = gridSumX[x-1][y+2]-gridSumX[x-1][y-1]
            same = gridSumX[x][y+2]-gridSumX[x][y-1]
            down = gridSumX[x+1][y+2]-gridSumX[x+1][y-1]
            if up==same and same == down:
                return True, up
            return False, 0
        def getHorizontalSumCheck(x, y):
            nonlocal gridSumY
            left = gridSumY[x+2][y-1]-gridSumY[x-1][y-1]
            same = gridSumY[x+2][y]-gridSumY[x-1][y]
            right = gridSumY[x+2][y+1]-gridSumY[x-1][y+1]
            if left==same and same == right:
                return True, same
            return False, 0
        magicCnt = 0
        uniSum = 45
        def checkUni(x,y):
            appear = [False]*9
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if grid[x+i][y+j]<1 or grid[x+i][y+j]>9:
                        return False
                    # print(grid[x+i][y+j])
                    if appear[grid[x+i][y+j]-1]:
                        return False
                    appear[grid[x+i][y+j]-1] = True
            return True
        for x in range(1, rows-1):
            for y in range(1, cols-1):
                vBool, vSum = getVerticalSumCheck(x,y)
                hBool, hSum = getHorizontalSumCheck(x,y)
                if not vBool or not hBool or vSum!=hSum:
                    continue
                if checkBothDiagonal(vSum, x, y):
                    if 3*vSum == uniSum and checkUni(x,y):
                        magicCnt+=1
        return magicCnt
                
        
        