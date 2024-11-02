class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # since it's consectutive then we use sliding window to count the 0 and 1
        # if the 0 cnt is less than k, then it's valid
        # always keep the expanding right while keeping left valid
        # time:O(N) space:O(1)
        left = 0
        ret = 0
        oneCnt = zeroCnt = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCnt += 1
                while zeroCnt>k:
                    if nums[left] == 0:
                        zeroCnt -= 1
                    left += 1
            now = right-left+1
            ret = max(ret, now)
        return ret