class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force is trying from speed 1 to max(pile[i])
        # time: O(nm) space:O(1)
        # binary search for 1...m
        # time: O(n*log(m)) space:O(1)
        def finishBana(k:int):
            useHour = 0
            for pile in piles:
                useHour += math.ceil(pile/k)
            if useHour <= h:
                return True
            return False
        left = 1
        right = max(piles)
        while left< right:
            mid = (left+right)//2
            if finishBana(mid):
                right = mid
            else:
                left = mid+1
        return right

