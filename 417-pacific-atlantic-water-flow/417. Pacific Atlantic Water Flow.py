class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs from one end , then try the other side
        # time:O(N) space:O(N)
        n = len(heights)
        m = len(heights[0])
        touchPacific = [[0 for x in range(m)] for y in range(n)]
        meet = []

        for i in range(n):
            meet.append([i,0])
            touchPacific[i][0] = 1
        for j in range(m):
            if touchPacific[0][j]==0:
                meet.append([0,j])
                touchPacific[0][j] = 1
        while len(meet)>0:
            levelCnt = len(meet)
            for i in range(levelCnt):
                nowX, nowY = meet.pop(0)
                curHeight = heights[nowX][nowY]
                # 4 direction if the height of neighbor is higher
                if nowX-1>=0 and touchPacific[nowX-1][nowY]==0:
                    if heights[nowX-1][nowY]>=curHeight:
                        meet.append([nowX-1,nowY])
                        touchPacific[nowX-1][nowY] = 1
                
                if nowX+1<n and touchPacific[nowX+1][nowY]==0:
                    if heights[nowX+1][nowY]>=curHeight:
                        meet.append([nowX+1,nowY])
                        touchPacific[nowX+1][nowY] = 1
                if nowY-1>=0 and touchPacific[nowX][nowY-1]==0:
                    if heights[nowX][nowY-1]>=curHeight:
                        meet.append([nowX,nowY-1])
                        touchPacific[nowX][nowY-1] = 1
                
                if nowY+1<m and touchPacific[nowX][nowY+1]==0:
                    if heights[nowX][nowY+1]>=curHeight:
                        meet.append([nowX,nowY+1])
                        touchPacific[nowX][nowY+1] = 1
        ret = []
        # print(touchPacific)
        # the head of Atlantic
        for i in range(n):
            meet.append([i,m-1])
            if touchPacific[i][m-1] == 1:
                ret.append([i,m-1])
            touchPacific[i][m-1] = 2
        for j in range(m-1):
            if touchPacific[n-1][j]==1:
                ret.append([n-1,j])
            meet.append([n-1,j])
            touchPacific[n-1][j] = 2
        
        while len(meet)>0:
            levelCnt = len(meet)
            for i in range(levelCnt):
                nowX, nowY = meet.pop(0)
                curHeight = heights[nowX][nowY]
                # 4 direction if the height of neighbor is higher
                if nowX-1>=0 and (touchPacific[nowX-1][nowY]==0 or touchPacific[nowX-1][nowY]==1):
                    if heights[nowX-1][nowY]>=curHeight:
                        meet.append([nowX-1,nowY])
                        if touchPacific[nowX-1][nowY]==1:
                            ret.append([nowX-1,nowY])
                        touchPacific[nowX-1][nowY] = 2
                
                if nowX+1<n and (touchPacific[nowX+1][nowY]==0 or touchPacific[nowX+1][nowY]==1):
                    if heights[nowX+1][nowY]>=curHeight:
                        meet.append([nowX+1,nowY])
                        if touchPacific[nowX+1][nowY]==1:
                            ret.append([nowX+1,nowY])
                        touchPacific[nowX+1][nowY] = 2
                if nowY-1>=0 and (touchPacific[nowX][nowY-1]==0 or touchPacific[nowX][nowY-1]==1):
                    if heights[nowX][nowY-1]>=curHeight:
                        meet.append([nowX,nowY-1])
                        if touchPacific[nowX][nowY-1]==1:
                            ret.append([nowX,nowY-1])
                        touchPacific[nowX][nowY-1] = 2
                
                if nowY+1<m and (touchPacific[nowX][nowY+1]==0 or touchPacific[nowX][nowY+1]==1):
                    if heights[nowX][nowY+1]>=curHeight:
                        meet.append([nowX,nowY+1])
                        if touchPacific[nowX][nowY+1]==1:
                            ret.append([nowX,nowY+1])
                        touchPacific[nowX][nowY+1] = 2
        
        # print(touchPacific)
        return ret
