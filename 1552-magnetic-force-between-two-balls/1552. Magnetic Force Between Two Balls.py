class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        def canPlaceBall(dist):
            nonlocal position, n, m
            prev = position[0]
            left = m-1
            for i in range(1,n):
                if position[i]-prev>=dist:
                    left-=1
                    prev = position[i]
                if left == 0:
                    return True
            return False
        if m==2:
            return position[n-1]-position[0]
        # longDist = (position[n-1]-position[0])//(m)+1
        longDist = (position[n-1])//(m-1)+1
        l = 0
        r = longDist
        # print(l,r)
        ret = 0
        while l<=r:
            mid = (l+r)//2
            if canPlaceBall(mid):
                ret = mid
                l = mid+1
            else:
                r = mid-1
        return ret

