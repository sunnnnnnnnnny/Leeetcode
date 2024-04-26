class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy similar to bottom-up from right concept
        # if any position from left can reach the lastIdx
        # meaning its good, so we update the lastIdx as it
        lastIdx = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= lastIdx:
                lastIdx = i
        return lastIdx==0


        # bottom-up with memo which starting from the right most
        # then update the previous step j can jump from i
        # also stop checking more j when i is good
        # cost: O(n^2) as we recursive at most 2 for loop
        # Good, Bad, Unknown = 1, 0, -1
        # canReverse = [Unknown]*len(nums)
        # lastIdx = len(nums)-1
        # canReverse[lastIdx] = Good
        # for i in range(lastIdx-1, -1, -1):
        #     furthestJumpIdx = min(i+nums[i], lastIdx)
        #     for j in range(i+1, furthestJumpIdx+1, 1):
        #         if canReverse[j] == Good:
        #             canReverse[i] = Good
        #             break
            
        # return canReverse[0] == Good

        # bottom-up by recording if any step can be jumped on
        # dp[i] = True if(dp[i-j] and i+nums[j] == i)
        # canReach = [False]*(len(nums))
        # lastIdx = len(nums)-1
        # canReach[0] = True
        # for i in range(len(nums)):
        #     if canReach[i]:
        #         for j in range(1, nums[i]+1, 1):
        #             # no need to care the rest
        #             if i+j>=len(nums):
        #                 break
        #             canReach[i+j] = True
        #             if i+j == lastIdx:
        #                 return True

        # # print(canReach)
        # return canReach[len(nums)-1]
        