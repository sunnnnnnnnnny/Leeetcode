class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(nums[i]+dp[i+2], dp[i+11])
        # botton-up
        # dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        if len(nums)==1:
            return nums[0]
        dpMoney = ([0]*len(nums))
        dpMoney[0] = nums[0]
        dpMoney[1] = max(nums[0], nums[1])
        # could replace the dpMoney List as only recording the prev 2 nums
        # thus the space can be saved from O(N)->O(1)
        for i in range(2, len(nums), 1):
            dpMoney[i] = max(nums[i]+dpMoney[i-2], dpMoney[i-1])
        return dpMoney[len(nums)-1]
