class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k>len(nums):
            return 0
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, [-nums[i], i])
        ret = 0
        idx = 0
        for i in range(1,k):
            now = heapq.heappop(pq)
        now = heapq.heappop(pq)
        ret = -now[0]
        idx = now[1]
        # print(ret, idx)
        return ret
        