class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # bfs when a single point having all count of friends
        # time: O(f*N*M) space:O(f*N*M)
        targetCnt = 0
        friendLoc = []
        n =len(grid)
        m = len(grid[0])
# simple math would be the using the mean of x cords and y cords
        # time:O(n*M+nlogn+mlogm) space:O(1)
        cordX = []
        cordY = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    targetCnt+=1
                    cordX.append(i)
                    cordY.append(j)
        cordX.sort()
        cordY.sort()
        def getMinDist(arrLoc, maxLen):
            i=0
            j = maxLen-1
            ret = 0
            while i<j:
                ret+=(arrLoc[j]-arrLoc[i])
                i+=1
                j-=1
            return ret
        return getMinDist(cordX, targetCnt)+getMinDist(cordY, targetCnt)
        # timeout
        # visited = {}
        # seenCnt = [[[0,0] for i in range(m)] for j in range(n)]
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 1:
        #             friendLoc.append([i,j,targetCnt])
        #             visited[targetCnt] = set()
        #             visited[targetCnt].add((i, j))
        #             targetCnt +=1
        # dist = 0
        # ret = -1
        # while friendLoc:
        #     levelCnt = len(friendLoc)
        #     for i in range(levelCnt):
        #         nowi, nowj, friendIdx = friendLoc.pop(0)
        #         seenCnt[nowi][nowj][0]+=1
        #         seenCnt[nowi][nowj][1]+=dist
        #         if seenCnt[nowi][nowj][0] == targetCnt:
        #             # print(nowi, nowj, friendIdx, dist)
        #             # return seenCnt[nowi][nowj][1]+dist
        #             ret = min(ret, seenCnt[nowi][nowj][1]) if ret!=-1 else seenCnt[nowi][nowj][1]
        #         if nowi-1>=0 and (nowi-1, nowj) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi-1, nowj))
        #             friendLoc.append((nowi-1, nowj, friendIdx))
        #         if nowi+1<n and (nowi+1, nowj) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi+1, nowj))
        #             friendLoc.append((nowi+1, nowj, friendIdx))
        #         if nowj-1>=0 and (nowi, nowj-1) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi, nowj-1))
        #             friendLoc.append((nowi, nowj-1, friendIdx))
        #         if nowj+1<m and (nowi, nowj+1) not in visited[friendIdx]:
        #             visited[friendIdx].add((nowi, nowj+1))
        #             friendLoc.append((nowi, nowj+1, friendIdx))
        #     dist+=1
        # return ret
        