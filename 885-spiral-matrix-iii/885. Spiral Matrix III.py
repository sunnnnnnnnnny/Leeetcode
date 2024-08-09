class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        visit = [(rStart, cStart)]
        # the regular is every 2 step having +1 moves
        # right 1, down 1, left 2, up 2, right 3, down 3
        # time: max(row, col)^2 b/cthe sprial size is adding up from 1, 2...row/col
        # space: row*col
        def nextDirection(dirct):
            if dirct == (0,1): 
                # right to down
                return (1,0)
            elif dirct == (0,-1):
                # left to up
                return (-1,0)
            elif dirct == (1,0):
                # down to left
                return (0,-1)
            else:
                # up to right
                return (0,1)
        def locValid(x, y):
            nonlocal rows, cols
            if x<0 or x>=rows:
                return False
            if y<0 or y>=cols:
                return False
            return True
        moveCnt = 0
        totalCnt = rows*cols
        rNow, cNow = rStart, cStart
        nDirect = (0,1)
        while len(visit)<totalCnt:
            stageMoves = (moveCnt//2)+1
            for _ in range(stageMoves):
                rNow += nDirect[0]
                cNow += nDirect[1]
                if locValid(rNow, cNow):
                    visit.append((rNow, cNow))
            nDirect = nextDirection(nDirect)
            moveCnt += 1
        return visit