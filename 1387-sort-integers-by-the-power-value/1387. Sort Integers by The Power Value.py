class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # get all the power of the num in lo~hi
        # use maxHeap to get the Kth num of min-power
        # time:O(NMlogK) where M is the time to transform into 1
        transPower = {}
        def getPower(x):
            if x== 1:
                return 0
            if x in transPower:
                return transPower[x]
            newX = x//2 if x%2==0 else 3*x+1
            po = getPower(newX)+1
            transPower[x] = po
            return po
        
        maxHeap = []
        for i in range(lo, hi+1):
            nowPo = getPower(i)
            if maxHeap and len(maxHeap)==k:
                topPower, topI = maxHeap[0]
                if -topPower>nowPo:
                    heapq.heappop(maxHeap)
                    # need the idx also be maxHeap, so the smaller index would be at bottom
                    heapq.heappush(maxHeap, [-nowPo, -i])
            else:
                heapq.heappush(maxHeap, [-nowPo, -i])
        topPower, topI = maxHeap[0]
        # print(getPower(2))
        # print(transPower)
        return -topI
