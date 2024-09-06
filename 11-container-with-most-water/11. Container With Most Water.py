class Solution:
    def maxArea(self, height: List[int]) -> int:
        # need to find the height on 2 ends
        # 2pointer to move from the two ends
        # move the shorter edge b/c it only have a chance be larger area while having higher end
        # assume hieght>0
        left = 0
        right = len(height)-1
        maxArea = min(height[left], height[right])*(right-left)
        while left<right:
            nowArea = min(height[left], height[right])*(right-left)
            maxArea = max(maxArea, nowArea)
            # print(nowArea, left, right)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea
