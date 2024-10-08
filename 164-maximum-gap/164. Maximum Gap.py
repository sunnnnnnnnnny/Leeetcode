class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # sorted it then check the gaps
        # time: O(nlogn+n) space:O(1)
        nums.sort()
        maxGap = 0
        for i in range(len(nums)-1, 0, -1):
            gap = nums[i]-nums[i-1]
            maxGap = max(maxGap, gap)
        return maxGap