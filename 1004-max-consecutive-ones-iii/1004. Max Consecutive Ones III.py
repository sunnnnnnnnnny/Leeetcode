class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # for consecutive ones it's a sliding window, 
        # by having the cnt of 0 in the window to determine the window is valid
        # time:O(N) space:O(1) just the count of 0 in the string
        start = 0
        zCnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zCnt+=1
            if zCnt>k:
                # always keep the maxValidWindowSize
                if nums[start] == 0:
                    zCnt -=1
                start += 1
        
        nowLen = len(nums)-start
        return nowLen
            