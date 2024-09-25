class KthLargest:
# need to keep track of the top k largest with a minHeap
# while the max size is K
# time: O(NlogK) with ignoring any num smaller than K
# space:O(K)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.topK = []
        for n in nums:
            if len(self.topK)<k:
                heapq.heappush(self.topK, n)
            else:
                topK = self.topK[0]
                if topK<n:
                    heapq.heappop(self.topK)
                    heapq.heappush(self.topK, n)

    def add(self, val: int) -> int:
        if len(self.topK)<self.k:
            heapq.heappush(self.topK, val)
        else:
            topK = self.topK[0]
            if topK<val:
                heapq.heappop(self.topK)
                heapq.heappush(self.topK, val)
        return self.topK[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)