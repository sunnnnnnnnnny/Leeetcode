class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # since we want smallest sum from the pair, we should only move the pointer of the smaller nums
        # treat it as merge k sorted array, with the head as first array for the move, we will use minHeap to get the data
        # N for idx1 M for idx2
        # time:O(Klog(N)) space:O(N)
        firstRowSum = []
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            nowSum = nums1[i]+nums2[0]
            heapq.heappush(firstRowSum, [nowSum, i, 0])
        ret = []
        for _ in range(k):
            if firstRowSum:
                nowS, idx1, idx2 = heapq.heappop(firstRowSum)
                ret.append([nums1[idx1], nums2[idx2]])
                if idx1<n and idx2+1<m:
                    newS = nums1[idx1]+ nums2[idx2+1]
                    heapq.heappush(firstRowSum, [newS, idx1, idx2+1])
        return ret