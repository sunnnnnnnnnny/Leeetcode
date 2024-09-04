class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # precalculate the prefix, suffix array up to current point
        # then going through the array we can get the product by prefix[i]*suffic[i+1]
        prefix = [1]*(len(nums)+1)
        suffix = [1]*(len(nums)+1)
        n = len(nums)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]*nums[i]
            sIdx = n-i-1
            suffix[sIdx] = suffix[sIdx+1]*nums[sIdx]
        ret = [0]*n
        for i in range(n):
            ret[i] = prefix[i]*suffix[i+1]
        return ret
        