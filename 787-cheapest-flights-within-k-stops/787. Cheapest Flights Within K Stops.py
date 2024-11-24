class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # diasktra with minHeap picking the next location
        # no negative cost edge, time:O(N) space:O(M) M is size of the edge
        edge = DefaultDict(dict)
        for connect in flights:
            fromA, toB, price = connect
            edge[fromA][toB] = price
        minHeap = []
        heapq.heappush(minHeap, [0, 0, src])
        costReach = {}
        while minHeap:
            nowCost, connectCnt, nowI = heapq.heappop(minHeap)
            if nowI in costReach:
                step, cost = costReach[nowI]
                if connectCnt>step:
                    continue
                
            costReach[nowI] = [connectCnt, nowCost]
            if nowI == dst:
                return nowCost
            if connectCnt <= k:
                for nextI, cost in edge[nowI].items():
                    heapq.heappush(minHeap, [nowCost+cost, connectCnt+1, nextI])
        return -1
                        
        