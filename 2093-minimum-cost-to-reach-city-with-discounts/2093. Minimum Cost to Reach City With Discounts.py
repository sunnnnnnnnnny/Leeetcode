class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        # use dfs/bfs to get all (x)
        # disjtra, with discount to record the move
        # Let N be the number of nodes (cities) and E be the number of edges (highways). Let K be the number of discounts.
        # Time Complexity: O((N⋅K+E)⋅log(N⋅K))
        # space:O(N*K+E)
        cost2Reach = [-1]*n
        cost2Reach[0] = 0
        # cost2Reach[0][discounts]=0
        link = {}
        # assume no duplicate c1,c2 pair
        for connect in highways:
            c1, c2, toll = connect
            if c1 not in link.keys():
                link[c1] = {}
            if c2 not in link.keys():
                link[c2] = {}
            link[c1][c2] = toll
            link[c2][c1] = toll
            # link[c1].append((c2,toll))
            # link[c2].append((c1,toll))
        # cost, useDiscount, nodeIdx so far
        nextCost = [(0,0,0)]
        visited = [[-1 for _ in range(discounts+1)]for _ in range(n)]
        while nextCost:
            nowCost, useDiscount, nowUpdateIdx = heapq.heappop(nextCost)
            # print(nowCost, useDiscount, nowUpdateIdx)
            if visited[nowUpdateIdx][useDiscount] != -1:
                continue
            visited[nowUpdateIdx][useDiscount] = 1
            if nowUpdateIdx in link.keys():
                for key, cost in link[nowUpdateIdx].items():
                    if cost2Reach[key] == -1:
                        newCost = cost+nowCost
                        heapq.heappush(nextCost,(newCost, useDiscount, key))
                        if useDiscount<discounts:
                            newCost = cost//2+nowCost
                            heapq.heappush(nextCost,(newCost, useDiscount+1, key))
                        cost2Reach[key] = newCost
                    else:
                        # doesn't matter if the cost is lower, we need to push into queue
                        # because the discount in later stage may be better usage
                        newCost = cost+nowCost
                        heapq.heappush(nextCost,(newCost, useDiscount, key))
                        if cost2Reach[key]>=newCost:
                            cost2Reach[key] = newCost
                        if useDiscount<discounts:
                            newCost = cost//2+nowCost
                            heapq.heappush(nextCost,(newCost, useDiscount+1, key))
                            if cost2Reach[key]>=newCost:
                                cost2Reach[key] = newCost
        target = n-1
        print(cost2Reach)
        return cost2Reach[target]


                
        
        