class MedianFinder:
    # use 2 heap, min (for large num) & max (small) to record the add num
    # always keep them len(max)-len(min)<=1
    # so we can get the median at the top or the (min_top+max_top)/2

    def __init__(self):
        self.maxHeapForSmall = []
        self.smallSize = 0
        self.minHeapForLarge = []
        self.largeSize = 0
        
# time: O(logN/2) for each add
# space: O(N)
    def addNum(self, num: int) -> None:
        if self.smallSize<self.largeSize:
            # add to small
            toSmall = num
            if num > self.minHeapForLarge[0]:
                toSmall = heapq.heappop(self.minHeapForLarge)
                heapq.heappush(self.minHeapForLarge, num)
            heapq.heappush(self.maxHeapForSmall, -toSmall)
            self.smallSize += 1

        else:
            # add to large
            toLarge = num
            if self.largeSize>0 and num < -self.maxHeapForSmall[0]:
                toLarge = -heapq.heappop(self.maxHeapForSmall)
                heapq.heappush(self.maxHeapForSmall, -num)
            heapq.heappush(self.minHeapForLarge, toLarge)
            self.largeSize+=1

# time: O(1) as we access the top item of both queue
# space: O(1)
    def findMedian(self) -> float:
        if self.largeSize==0 and self.smallSize==0:
            return 0
        if self.largeSize>self.smallSize:
            return self.minHeapForLarge[0]
        else:
            med = self.minHeapForLarge[0]-self.maxHeapForSmall[0]
            return med/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()