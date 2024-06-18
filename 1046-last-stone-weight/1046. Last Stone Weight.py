class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use maxHeap to get the largest 2 stones
        # pop the 2 stones and push it back
        # time: O(N)+O(N*3LogN) = O(NlogN)
        # space:O(N)
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        # print(maxHeap)
        while len(maxHeap)>1:
            s1 = -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)
            if s1-s2>0:
                heapq.heappush(maxHeap, s2-s1)
        return 0 if len(maxHeap)==0 else -heapq.heappop(maxHeap)

        