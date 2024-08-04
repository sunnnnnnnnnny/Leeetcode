class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # using minHeap(size: total-right) for larger num after right and 
        # maxHeap(left-1) for smaller num before left
        # by calculating the sum of subarray, putting into minheap or maxheap
        # heappop cost O(MlogM)
        # time; O(N*N*MlogM)? space:O(M*2)
        maxHeapLeft = []
        minHeapRight = []
        totalSize = (n*(n+1))//2
        leftSize = left-1
        rightSize = totalSize-right
        ret = 0
        m = 1000000007
        for i in range(n):
            tempSum = 0
            for j in range(i, n):
                tempSum += nums[j]
                now = tempSum
                # check the maxHeap see if smaller
                if len(maxHeapLeft)<leftSize:
                    heapq.heappush(maxHeapLeft, -now)
                    continue
                else:
                    if len(maxHeapLeft)>0 and -maxHeapLeft[0]>now:
                        temp = heapq.heappop(maxHeapLeft)
                        heapq.heappush(maxHeapLeft, -now)
                        now = -temp
                # check the minHeap see if larger
                if len(minHeapRight)<rightSize:
                    heapq.heappush(minHeapRight, now)
                    continue
                else:
                    if len(minHeapRight)>0 and minHeapRight[0]<now:
                        temp = heapq.heappop(minHeapRight)
                        heapq.heappush(minHeapRight, now)
                        now = temp
                ret += now
                ret = ret%m
        # print(maxHeapLeft)
        # print(minHeapRight)
        return ret
        