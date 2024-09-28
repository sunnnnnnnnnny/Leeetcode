class Solution:
    def findGroup(self, x, groupList):
        if groupList[x]!=x:
            return self.findGroup(groupList[x], groupList)
        return groupList[x]
    def combineGroup(self, x,y, groupList, rankList):
        xG = self.findGroup(x, groupList)
        yG = self.findGroup(y, groupList)
        if xG!=yG:
            if rankList[xG]>rankList[yG]:
                groupList[yG] = xG
                rankList[xG]+=1
            else:
                groupList[xG] = yG
                rankList[yG]+=1

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # getting all the dist, and always add the least dist cost to the graph
        # but only select the one not in the graph yet
        n = len(points)
        group = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        distList = []
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(distList, (dist, i,j))
        ret = 0
        while distList:
            nowDist, x,y = heapq.heappop(distList)
            xG = self.findGroup(x, group)
            yG = self.findGroup(y, group)
            if xG != yG:
                ret += nowDist
                self.combineGroup(x,y,group, rank)
        return ret