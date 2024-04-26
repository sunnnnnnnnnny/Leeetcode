class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # bottom-up by recording if any step can be jumped on
        # dp[i] = True if(dp[i-j] and i+nums[j] == i)
        canReach = [False]*(len(nums))
        lastIdx = len(nums)-1
        canReach[0] = True
        for i in range(len(nums)):
            if canReach[i]:
                for j in range(1, nums[i]+1, 1):
                    # no need to care the rest
                    if i+j>=len(nums):
                        break
                    canReach[i+j] = True
                    if i+j == lastIdx:
                        return True

        # print(canReach)
        return canReach[len(nums)-1]
        