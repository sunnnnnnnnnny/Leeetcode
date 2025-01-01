class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # since it's max num then sort the banned then start adding from 1 to n
        # time:O(mlogm+n) space:O(m)
        # banned.sort()
        banned = set(banned)
        l = 0
        h = n
        while l<h:
            mid = (l+h+1)//2
            # mid = l + h + 1 >> 1
            total = mid*(mid+1)//2
            for x in banned:
                if x<=mid:
                    total -= x
            if total<=maxSum:
                l = mid
            else:
                h = mid-1
        return l - sum(x <= l for x in banned)