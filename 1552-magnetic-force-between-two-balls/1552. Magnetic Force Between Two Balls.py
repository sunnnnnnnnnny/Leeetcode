class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # similar to koko banana, use binary search for the space
        # range from 1 to lastPos-firstPos//m
        # where Y = lastPos-firstPos//m
        # sorting and checking the fit take O(N) with binary search logY
        # sorting takes the space of O(N) in python
        # time:O(NlogY+NlogN)=O(NlogY*N) space:O(N)
        position.sort()
        def canFit(dist):
            nonlocal position, m
            prePos = position[0]
            leftBall = m-1
            for i in range(1, len(position)):
                if position[i]>=prePos+dist:
                    prePos = position[i]
                    leftBall -= 1
                if leftBall==0:
                    break
            return True if leftBall==0 else False
        left = 1
        right = (position[-1]-position[0])//(m-1)
        print(left, right)
        while left<=right:
            mid = (left+right)//2
            isFit = canFit(mid)
            if isFit:
                left = mid+1
            else:
                right = mid-1
        # rightFit = canFit(right)
        # print(right, rightFit)
        
        return right