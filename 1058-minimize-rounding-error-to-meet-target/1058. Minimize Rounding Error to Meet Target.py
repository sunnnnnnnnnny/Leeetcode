class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        # greedy, check if the result can be within the range
        # then start with the min and flip the price with least cost
        # time:O(NlogN)
        # (wrong)dp with each number choosing to be floor or ceil
        # time:O(N^2) space:O(N^2)
        minN = sum([math.floor(float(p)) for p in prices])
        maxN = sum([math.ceil(float(p)) for p in prices])
        if target<minN or target>maxN:
            return "-1"
        diffCost = []
        idx = 0
        for p in prices:
            celiCost = round(math.ceil(float(p)) - float(p),3)
            floorCost = round(float(p) - math.floor(float(p)),3)
            heapq.heappush(diffCost, (celiCost-floorCost, idx))
            idx += 1
        needCost = target-minN
        ret = 0.000
        for i in range(needCost):
            nowDiff, idx = heapq.heappop(diffCost)
            p = prices[idx]
            # take celi
            nowAdd = round(math.ceil(float(p)) - float(p),3)
            # print(nowAdd, idx)
            ret += nowAdd
        while diffCost:
            nowDiff, idx = heapq.heappop(diffCost)

            # take celi
            p = prices[idx]
            nowAdd = round(float(p) - math.floor(float(p)),3)
            # print(nowAdd, idx)
            if nowAdd<1:
                ret += nowAdd
        retStr = "{:.3f}".format(ret)
        return retStr
