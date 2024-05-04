class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = [-1, 0], [1, 0], [0, -1], [0, 1]
        def nextDir(curDir):
            if curDir == up:
                return right
            if curDir == down:
                return left
            if curDir == left:
                return up
            return down
        def nextIdx(curDir, x, y):
            if curDir == up:
                return x+up[0], y+up[1]
            if curDir == down:
                return x+down[0], y+down[1]
            if curDir == left:
                return x+left[0], y+left[1]
            return x+right[0], y+right[1]
        ret = []
        upLimit = 0
        downLimit = len(matrix)
        leftLimit = 0
        rightLimit = len(matrix[0])
        nowDir = right
        totalItem = downLimit*rightLimit
        xIdx, yIdx = 0,0
        # print('limit: downLimit: rightLimit:', downLimit, rightLimit)
        while len(ret)<totalItem:
            ret.append(matrix[xIdx][yIdx])
            nextX, nextY = nextIdx(nowDir, xIdx, yIdx)
            # print('next ', nextX, nextY)
            if nextX>=downLimit or nextX<upLimit or nextY>=rightLimit or nextY<leftLimit:
                nowDir = nextDir(nowDir)
                if nowDir == up:
                    downLimit -= 1
                if nowDir == down:
                    upLimit += 1
                if nowDir == left:
                    rightLimit -= 1
                if nowDir == right:
                    leftLimit += 1
                nextX, nextY = nextIdx(nowDir, xIdx, yIdx)
            
            # print('next ', nextX, nextY)
            xIdx = nextX
            yIdx = nextY
            # print('idx ', xIdx, yIdx)
            # print(ret)
        return ret
            

