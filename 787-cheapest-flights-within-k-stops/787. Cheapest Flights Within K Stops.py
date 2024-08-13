class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford for k loops, run all edges
        # time: O(k*E) space:O(n)
        curDist = [math.inf]*n
        curDist[src] = 0
        preDist = [math.inf]*n
        preDist[src] = 0
        for _ in range(k+1):
            for edge in flights:
                s, d, p = edge
                newcost = preDist[s]+p
                curDist[d] = min(newcost, curDist[d])
            # print(preDist)
            # print(curDist)
            preDist = copy.deepcopy(curDist)
        
        if preDist[dst]<math.inf:
            return preDist[dst]
        return -1


        