class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using a minHeap of size k, every time getting a new larger num than the head of minHeap
        # pop it and added in, after going through the whole nums, the head of minHeap is the result
        # time:O(NlogK) space:O(K)
        n = len(nums)
        if k>n:
            return -1
        minH = []
        heapq.heapify(minH)
        for n in nums:
            if len(minH)>=k:
                if n>minH[0]:
                    heapq.heappop(minH)
                    heapq.heappush(minH, n)
            else:
                heapq.heappush(minH, n)
        return minH[0]