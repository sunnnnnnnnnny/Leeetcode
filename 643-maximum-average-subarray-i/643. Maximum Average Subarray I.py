class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window? time: O(N) spaace:O(1)
        maxK = 0
        for i in range(k):
            maxK += nums[i]
        nowK = maxK
        j = 0
        for i in range(k, len(nums)):
            nowK += nums[i]
            nowK -= nums[j]
            j += 1
            maxK = max(maxK, nowK)
        return maxK/k
