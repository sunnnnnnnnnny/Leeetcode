class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford, relax the edges for k+1 times
        # time:O((N+E)*K) space:O(N)
        # We are iterating over all the edges K+1 times which takes O(E⋅K). 
        # At the start and end of each iteration, we also swap distance arrays, 
        # which take O(N⋅K) time for all the iterations. 
        reCost = {}
        reCost[src] = 0
        for i in range(k+1):
            newCost = copy.deepcopy(reCost)
            for flight in flights:
                fromS, toD, cost = flight
                if fromS in reCost:
                    nextC = reCost[fromS]+cost
                    if toD not in newCost or newCost[toD]>nextC:
                        newCost[toD] = nextC
            reCost = newCost
        # print(reCost)
        return reCost[dst] if dst in reCost else -1