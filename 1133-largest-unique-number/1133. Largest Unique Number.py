class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # sort then traverse from the last
        # time:O(NlogN+N) space:O(1)
        # using a hashset to record the appread count, with maxHeap
        # time:O(NlogN) as add and pop for maxHeap takes time logN
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        i = n-1
        while i>0:
            if nums[i] == nums[i-1]:
                duplicateN = nums[i]
                while i>=0 and nums[i] == duplicateN:
                    i-=1
            else:
                return nums[i]
        
        return -1 if nums[0]==nums[1] else nums[0]

        