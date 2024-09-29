class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # relation = [[] for i in range(n+1)]
        # costArr = [-1 for i in range(n+1)]
        costArr = [-1]*(n+1)
        relationDict = {}
        for t in times:
            s,d,cost = t
            if s not in relationDict.keys():
                relationDict[s] = []
            relationDict[s].append((d,cost))
            # relation[s].append((d,cost))

        # disikija with getting the shorest
        pq = []
        heapq.heappush(pq, (0,k))
        maxDist = 0
        while pq:
            cost, now = heapq.heappop(pq)
            if costArr[now]>-1:
                continue
            costArr[now] = cost
            maxDist = max(maxDist, cost)
            if now in relationDict.keys():
                for i in relationDict[now]:
                    nextI, nextT = i
                    if costArr[nextI]>-1 and costArr[nextI]>cost+nextT:
                        continue
                    heapq.heappush(pq, (cost+nextT,nextI))
        
        for i in range(1, n+1):
            if costArr[i]==-1:
                return -1
        return maxDist

        # dfs with only traversing the time needed is less than current stored
        # def dfs(now, needTime):
        #     nonlocal costArr,relation
        #     # print(now, costArr[now], needTime)
        #     if costArr[now] > -1 and costArr[now]<needTime:
        #         return
        #     costArr[now]=needTime
        #     for d,c in relation[now]:
        #         dfs(d,needTime+c)
        #     return
        # dfs(k,0)
        # ret = -1
        # for i in range(1,n+1):
        #     if costArr[i] == -1:
        #         return -1
        #     if ret == -1 or ret<costArr[i]:
        #         ret = costArr[i]
        # return ret

