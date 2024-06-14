class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the min of speed should not be the min(pile) should be 1
        # koko speed k is min(piles)-max(piles)
        # since we eat no more than one pile, 
        # thus we have to find out what's the min k of it by helper functio
        def canFinish(k:int)->bool:
            needHour = 0
            for pile in piles:
                needHour += math.ceil(pile/k)
            if needHour<=h:
                return True
            return False
        left = 1
        right = max(piles)
        while left<=right:
            mid = left + (right-left)//2
            # print(left, right, mid)
            if canFinish(mid):
                right = mid-1
            else:
                left = mid+1
        return left


        # the speed will in btw of 1 and max() of the banana piles
        # need to check if it can be finished in h hours
        # binary search for the speed -> time O(NlogM) space:O(1)
        # def canFinishBanana(k):
        #     useHour = 0
        #     for pile in piles:
        #         useHour += math.ceil(pile/k)
        #     if useHour>h:
        #         return False
        #     return True
        # left = 1
        # right = max(piles)
        # while left<right:
        #     k = left+(right-left)//2
        #     if canFinishBanana(k):
        #         right = k
        #     else:
        #         left = k+1
        # return right
        # brute force is trying from speed 1 to max(pile[i])
        # time: O(nm) space:O(1)
        # binary search for 1...m
        # time: O(n*log(m)) space:O(1)
        # def finishBana(k:int):
        #     useHour = 0
        #     for pile in piles:
        #         useHour += math.ceil(pile/k)
        #     if useHour <= h:
        #         return True
        #     return False
        # left = 1
        # right = max(piles)
        # while left< right:
        #     mid = (left+right)//2
        #     if finishBana(mid):
        #         right = mid
        #     else:
        #         left = mid+1
        # return right

