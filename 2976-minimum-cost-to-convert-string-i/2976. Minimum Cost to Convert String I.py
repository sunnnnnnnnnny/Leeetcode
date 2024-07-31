class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # find all pairs of x to y, get the smallest cost of each pair
        # then the min cost is the sum
        # pairs change need N, cost map M , graph traversal for all N in M
        # Z is the len of source
        # time: O(NM+Z) space:O(M+Z) for building the graph
        ret = 0
        # build the graph
        costGraph = {}
        connect = {}
        for i in range(len(original)):
            key = (original[i], changed[i])
            if original[i] not in connect.keys():
                connect[original[i]] = set()
            connect[original[i]].add(changed[i])
            if key not in costGraph.keys():
                costGraph[key] = cost[i]
            else:
                costGraph[key] = min(costGraph[key], cost[i])
        # print(costGraph)
        # print(connect)
        # need to use dijkstra for getting the shorest cost from a to b
        def dijkstraMin(now):
            now2OtherCost = {}
            nonlocal costGraph, connect
            pqForNext = [(0,now)]
            while pqForNext:
                curCost, curChar = heapq.heappop(pqForNext)
                # already having the min cost from now
                if curChar in now2OtherCost.keys():
                    continue
                now2OtherCost[curChar] = curCost
                if curChar in connect.keys():
                    for nextTarget in connect[curChar]:
                        newCost = curCost+costGraph[(curChar, nextTarget)]
                        if nextTarget not in now2OtherCost.keys():
                            heapq.heappush(pqForNext, (newCost, nextTarget))
            return now2OtherCost
        convMinCost = {}
        for i in range(len(source)):
            if source[i] != target[i]:
                if source[i] not in convMinCost.keys():
                    convMinCost[source[i]] = dijkstraMin(source[i])
                # can't convert from source
                if target[i] not in convMinCost[source[i]].keys():
                    return -1

                ret += convMinCost[source[i]][target[i]]

        # def minCostChange(now, target, nowCost, minCost, visited):
        #     nonlocal costGraph, connect
        #     if now == target:
        #         minCost = min(minCost, nowCost) if minCost>0 else nowCost
        #         return minCost
        #     if now in connect.keys():
        #         # print(now,connect[now],  visited)
        #         for dest in connect[now]:
        #             if dest not in visited:
        #                 visited.add(dest)
        #                 newMinCost = minCostChange(dest, target, nowCost+costGraph[(now,dest)], minCost, visited)
        #                 if newMinCost>0:
        #                     minCost = min(minCost, newMinCost) if minCost>0 else newMinCost
        #                 visited.remove(dest)
        #     return minCost

        # convMinCost = {}
        # for i in range(len(source)):
        #     if source[i] != target[i]:
        #         key = (source[i], target[i])
        #         if key not in convMinCost.keys():
        #             minCostPair = minCostChange(source[i],target[i],0,-1,set(source[i]))
        #             if minCostPair<0:
        #                 return -1
        #             convMinCost[key] = minCostPair
        #             costGraph[key] = minCostPair
        #             connect[source[i]].add(target[i])
        #         ret += convMinCost[key]

        return ret