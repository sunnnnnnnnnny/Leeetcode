class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search to get the speend 1, max(pile)
        # time:O(log(max_pile)) space:O(1)
        def canFinish(eatSp):
            nonlocal piles, h
            usedH = 0
            for p in piles:
                usedH += (p//eatSp)
                if p%eatSp>0:
                    usedH+=1
            # print(eatSp, usedH)
            return usedH<=h
        right = max(piles)
        left = 1
        while left<right:
            mid = (left+right)//2
            if canFinish(mid):
                right = mid
            else:
                left = mid+1
        return right
        