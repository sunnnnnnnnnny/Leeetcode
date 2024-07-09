class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start from both sides, move the shorter edge to higher one
        # in order to increase the container size
        # time: O(N) space:O(1)
        left = 0
        right = len(height)-1
        maxSize = min(height[left], height[right])*(right-left)
        while left<right:
            curSize = min(height[left], height[right])*(right-left)
            maxSize = max(curSize, maxSize)
            if height[left]< height[right]:
                left+=1
            else:
                right -=1
        return maxSize
        