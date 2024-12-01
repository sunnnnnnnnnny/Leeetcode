class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # backtracking with memo of i being j color
        # time:O(2^N) with memo O(N) space:O(3N)
        n = len(costs)
        memo = {}
        colorS = len(costs[0])
        def bk(idx, color):
            nonlocal n, memo, colorS, costs
            if idx>=n:
                return 0
            if (idx,color) in memo:
                return memo[(idx,color)]
            # other color
            minCost = inf
            for i in range(colorS):
                if i!=color:
                    nowCost = bk(idx+1, i)
                    minCost = min(minCost, nowCost)
            minCost += costs[idx][color]
            memo[(idx, color)] = minCost
            return minCost
        ret = inf
        for j in range(colorS):
            ret = min(ret, bk(0, j))
        return ret