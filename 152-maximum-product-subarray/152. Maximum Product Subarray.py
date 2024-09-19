class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] = dp[i-1]max*self, dp[i-1]min*self, self
        # record the current min and max product till before
        # time:O(N) space:O(1)
        ret = nums[0]
        prevPos = 0
        prevNeg = 0
        for i in range(0, len(nums)):
            if nums[i]==0:
                prevPos = prevNeg = 0
                ret = max(0, ret)
                continue
            
            newPos = prevPos*nums[i]
            newNeg = prevNeg*nums[i]
            if nums[i]>0:
                curPos = max(newPos, nums[i])
                ret = max(curPos, ret)
                prevPos = curPos
                prevNeg = newNeg
            else:
                curNeg = min(newPos, nums[i])
                if prevNeg!=0:
                    ret = max(newNeg, ret)
                else:
                    ret = max(nums[i], ret)
                prevPos = newNeg
                prevNeg = curNeg
        return ret

                

