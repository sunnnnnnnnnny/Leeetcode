class Solution:
    def trap(self, height: List[int]) -> int:
        # get the hight from left and right, for each idx, the accumulated water is min(left, right)
        # time:O(N) space:O(N)
        n = len(height)
        rightHeight = [0] * n
        for i in range(n-2, -1, -1):
            rightHeight[i] = max(rightHeight[i+1], height[i+1])
        ret = 0
        leftH = 0
        for i in range(1, n):
            leftH = max(leftH, height[i-1])
            nowW = min(leftH, rightHeight[i])
            ret += nowW-height[i] if nowW>height[i] else 0
        return ret
        