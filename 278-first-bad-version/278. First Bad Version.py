# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search to always move to before if current is bad
        bad = n
        start = 1
        while start<bad:
            mid = (bad-start)/2+start
            if isBadVersion(mid):
                bad = mid
            else:
                start = mid+1
        return int(bad)
        