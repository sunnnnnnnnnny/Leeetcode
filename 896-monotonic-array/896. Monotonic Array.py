class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # determine it's increase or decrease
        # time:O(N) space:O(1)
        n = len(nums)
        for i in range(1, n):
            if nums[i]>=nums[i-1] and nums[n-1]>nums[0]:
                continue
            elif nums[i]<=nums[i-1] and nums[n-1]<nums[0]:
                continue
            elif nums[i]==nums[i-1] and nums[n-1]==nums[0]:
                continue
            return False
        return True