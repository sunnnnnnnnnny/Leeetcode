class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[n:1] = max(n+dp[n-2:2], dp[n-1:1])
        def dp(end, start):
            if start>end:
                return 0
            if start == end:
                return nums[start]
            if end-start == 1:
                return max(nums[start], nums[end])
            # print('start: end:',start, end)
            return max(nums[end]+dp(end-2,start), dp(end-1, start))
        def dp_simple(self, nums:List[int])-> int:
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            pre2 = nums[0]
            pre1 = max(nums[0], nums[1])
            now = max(nums[0], nums[1])
            for i in range(2, len(nums), 1):
                now = max(nums[i]+pre2, pre1)
                pre2 = pre1
                pre1 = now
            return now
        n= len(nums)-1
        if n<1:
            return nums[n]
        # print(nums[1:n+1])
        # print(nums[0:n])
        # to break the tie of connected cycle of first and last house
        dp_n_to_1 = dp_simple(self, nums[1:n+1])
        dp_nm1_to_0 = dp_simple(self, nums[0:n])
        return max(dp_n_to_1, dp_nm1_to_0)
