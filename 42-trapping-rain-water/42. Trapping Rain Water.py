class Solution:
    def trap(self, height: List[int]) -> int:
        # bruteforce by setting each point as start, check the nearest hiehgt for it
        # so we know it can trap the water
        n = len(height)
        # find the prefixLeft and prefixRight of trapped point then go to both end
        # time:O(N) space:O(2N) = O(N)
        maxLeft = [0]*n
        maxRight = [0]*n
        rIdx = n-1
        maxLeft[0] = height[0]
        maxRight[rIdx] = height[rIdx]
        for i in range(1,n):
            rIdx -= 1
            maxRight[rIdx] = max(height[rIdx], maxRight[rIdx+1])
            maxLeft[i] = max(height[i], maxLeft[i-1])
        ret = 0
        for i in range(1,n-1):
            if maxRight[i]>height[i] and maxLeft[i]>height[i]:
                ret += min(maxRight[i], maxLeft[i])-height[i]
        return ret