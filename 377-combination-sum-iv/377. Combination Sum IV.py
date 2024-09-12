class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # difference sequence is consider different
        # dp[i] = all sum of (dp[i-n])
        # time:O(target*nums) space:O(target)
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for t in range(1,target+1):
            for n in nums:
                if t-n>=0:
                    dp[t]+=dp[t-n]
        return dp[target]