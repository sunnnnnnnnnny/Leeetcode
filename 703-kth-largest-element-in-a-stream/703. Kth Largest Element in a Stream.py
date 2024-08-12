class KthLargest:
    # using a minHeap of size k, of all the large number 
    # assume the k <= len(nums)
    # time: O(MlogK) space:O(K)
    # overall time: O((M+N)⋅logk)
    kSmall = []
    K = -1
    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.kSmall = []
        for n in nums:
            if len(self.kSmall)<k:
                heapq.heappush(self.kSmall, n)
            else:
                if n > self.kSmall[0]:
                    heapq.heappop(self.kSmall)
                    heapq.heappush(self.kSmall, n)

    # add will compare to the top of the maxHeap, if larger not dealing
    # smaller then pop the top and add it, if total N add
    # time: O(1) if larger O(NlogK) if pop
    def add(self, val: int) -> int:
        if len(self.kSmall)<self.K:
            heapq.heappush(self.kSmall, val)
        else:
            if val > self.kSmall[0]:
                heapq.heappop(self.kSmall)
                heapq.heappush(self.kSmall, val)
        # print(val, len(self.kSmall))
        return self.kSmall[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)